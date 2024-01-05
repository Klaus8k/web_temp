import asyncio
import logging
from random import randint

from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils import exceptions

logging.basicConfig(level=logging.INFO)

what_it_is = '6241591643'
token_telegram = what_it_is + ":AAG3Fj6XQMejHi5-mLsc1rjKcKkyXDsYiYk"

bot = Bot(token=token_telegram, parse_mode=types.ParseMode.HTML)

dp = Dispatcher(bot=bot)

# Хэндлер исключений
bots_exeptions = [exceptions.BotBlocked,]


@dp.errors_handler(exception=bots_exeptions)
async def errors_bot(update: types.Update, exeption: object):
    pass


# Хэндлер ответа
@dp.message_handler(commands=['start', 'help', '1-10'])
async def cmd_start(message: types.Message):
    print(message)
    if message.get_command() == r'/start':
        await message.reply('Get start!@')
    elif message.get_command() == r'/help':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['Menu', 'random', 'Order']
        keyboard.add(*buttons)
        await message.answer('Menu:', reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == 'random')
async def random(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(
        'rand 1-100', callback_data='start_rand'))
    await message.answer('push the button', reply_markup=keyboard)


@dp.callback_query_handler(text='start_rand')
async def send_rand(call: types.CallbackQuery):
    await call.message.answer(str(randint(1, 100)))


@dp.message_handler(lambda message: message.text in ['order', 'Order'])
async def order(message: types.Message):
    await message.answer('Link to <a href="https://sokolol.ru/order_cost/">order</a>')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
