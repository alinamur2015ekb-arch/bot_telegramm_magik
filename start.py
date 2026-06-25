import asyncio
import os
import signal
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
import aiohttp
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from main.hendlers import router as hendlers_router
from main.hendlers_robotics import router as hendlers_router_robotics
from main.hendlers_python import router as hendlers_router_python
from main.my_command import router as my_command_router
from main.play1 import router as play1_router
from main.play2 import router as play2_router
from database import init_answer, init_play  

load_dotenv()
token = os.getenv("TOKEN")
if not token:
    raise RuntimeError("Не задан TOKEN в переменных окружения!")

dp = Dispatcher()
dp.include_routers(
    hendlers_router,
    hendlers_router_robotics,
    hendlers_router_python,
    my_command_router,
    play1_router,
    play2_router,
)

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Not Found')

    def log_message(self, format, *args):
        pass

def run_health_server():
    port_str = os.environ.get('PORT', '8000')
    try:
        port = int(port_str)
    except ValueError:
        print(f"Ошибка: PORT='{port_str}' не является числом. Используем порт 8000 по умолчанию.")
        port = 8000
    
    server_address = ('0.0.0.0', port)
    httpd = HTTPServer(server_address, HealthHandler)
    print(f"HTTP Health Server запущен на порту {port}")
    httpd.serve_forever()

async def pinger():
    """Пингует сам себя, чтобы Render не «усыплял» сервис"""
    await asyncio.sleep(15) 
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                url = os.environ.get('RENDER_EXTERNAL_URL')
                if not url:
                    print("Предупреждение: не задана переменная RENDER_EXTERNAL_URL. Пинги могут не работать.")
                    url = f"http://localhost:{os.environ.get('PORT', '8000')}"
                
                async with session.get(url, timeout=10) as response:
                    print(f"Пинг выполнен! Статус: {response.status}")
            except Exception as e:
                print(f"Ошибка пинга: {e}")
            await asyncio.sleep(600)  

async def main():
    bot = Bot(token)
    await bot.delete_webhook(drop_pending_updates=True)
    print("Вебхук удален, режим polling активирован.")
    print("Инициализация таблиц базы данных...")
    await init_answer() 
    await init_play()   
    print("Все таблицы успешно созданы и готовы к работе!")
    
    asyncio.create_task(pinger())
    
    print("Бот успешно запущен!")
    try:
        await dp.start_polling(bot)
    finally:
        await dp.storage.close()
        await bot.session.close()

def handle_sigterm(signum, frame):
    print("Получен сигнал завершения (SIGTERM). Остановка...")
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGTERM, handle_sigterm)
    
    threading.Thread(target=run_health_server, daemon=True).start()
    time.sleep(2)  # Даём серверу время запуститься и занять порт
    
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Бот остановлен пользователем!")
