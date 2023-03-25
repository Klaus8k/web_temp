import asyncio
import logging

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

token = "6241591643:AAG3Fj6XQMejHi5-mLsc1rjKcKkyXDsYiYk"

bot = Bot(token=token)

dp = Dispatcher(bot=bot)

@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await message.reply('Get start!@')



# if __name__ == '__main__':

executor.start_polling(dp, skip_updates=True)


