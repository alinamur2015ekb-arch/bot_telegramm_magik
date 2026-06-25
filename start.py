import asyncio
import os
import signal
import sys
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

async def main():
    bot = Bot(token)
    
    await bot.delete_webhook(drop_pending_updates=True)
    print("Вебхук удален, режим polling активирован.")

    print("Инициализация таблиц базы данных...")
    await init_answer() 
    await init_play()   
    print("Все таблицы успешно созданы и готовы к работе!")
    
    print("Бот успешно запущен!")
    await dp.start_polling(bot)

def handle_sigterm(signum, frame):
    print("Получен сигнал завершения (SIGTERM). Остановка...")
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGTERM, handle_sigterm)
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Бот остановлен!")
