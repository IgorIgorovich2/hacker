import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message


bot = Bot(token = '7780233707:AAHTkCly0FqArzyqSjJtgLMKvYRwVNda5ic')
dp = Dispatcher()


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
