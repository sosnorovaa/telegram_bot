import logging
import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv

# Загружаем токен
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Проверяем, загружен ли токен
if not TOKEN:
    raise ValueError("❌ Токен не найден. Проверь настройки!")

# Инициализируем бота
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Команда /start
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Я бот для отправки шаблонов. Напиши /шаблоны, чтобы увидеть список.")

# Функция для запуска бота
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

# Запуск бота
if __name__ == "__main__":
    asyncio.run(main())
