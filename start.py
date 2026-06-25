import asyncio
import os
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


class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')
        else:
            # На всё остальное тоже можно отвечать 404
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Not Found')

    def log_message(self, format, *args):
        pass

def run_health_server():
    port = int(os.environ.get('PORT', 8000))
    server_address = ('0.0.0.0', port)
    httpd = HTTPServer(server_address, HealthHandler)
    httpd.serve_forever()

async def pinger():
    """Функция, которая сама пингует сайт бота, чтобы он не спал"""
    await asyncio.sleep(10)
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                
                async with session.get('https://telegramm-bot-rpin.onrender.com') as response:
                    print(f"Пинг выполнен! Статус: {response.status}")
            except Exception as e:
                print(f"Ошибка пинга: {e}")
            await asyncio.sleep(600)


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

async def main():
    bot = Bot(token)
    print("Инициализация таблиц базы данных...")
    await init_answer() 
    await init_play()   
    print("Все таблицы успешно созданы и готовы к работе!")
    
    asyncio.create_task(pinger())
    
    print("Бот успешно запущен, пингер работает!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    threading.Thread(target=run_health_server, daemon=True).start()
    
    time.sleep(1)
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Бот остановлен!")
