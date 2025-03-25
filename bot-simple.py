from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()
# Токен вашего бота, полученный от BotFather в Telegram
TOKEN = os.getenv("BOT_TOKEN")

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def send_welcome(message: Message):
    await message.answer("Привет! Я ваш бот. Напишите /help для получения списка команд.")

# Обработчик команды /help
@dp.message(Command("help"))
async def send_help(message: Message):
    help_text = (
        "Список доступных команд:\n"
        "/start - Начать общение с ботом\n"
        "/help - Получить помощь\n"
        "Также вы можете отправить любое текстовое сообщение, и я его повторю."
    )
    await message.answer(help_text)

# Обработчик текстовых сообщений
@dp.message()
async def echo(message: Message):
    # Бот просто повторяет сообщение пользователя
    await message.reply(f"Вы написали: {message.text}")

# Запуск бота
async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())