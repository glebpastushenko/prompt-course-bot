# Точка входа для запуска бота
from handlers import dp
from aiogram import executor

if __name__ == '__main__':
    from config import TOKEN
    from aiogram import Bot
    bot = Bot(token=TOKEN)
    executor.start_polling(dp)