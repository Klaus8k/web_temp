import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command


logging.basicConfig(level=logging.INFO)

token = "6241591643:AAG3Fj6XQMejHi5-mLsc1rjKcKkyXDsYiYk"

bot = Bot(token=token)

dp = Dispatcher()

@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.reply('test all right')

async def main():
    await dp.start_polling(bot)



# if __name__ == '__main__':

asyncio.run(main())



