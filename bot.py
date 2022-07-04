"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging

import wikipedia
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5395469079:AAFI449HSupoVr4PGRAI75wQo5fnZWQ1K64'

# leng
wikipedia.set_lang('uz')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply(
        f"Assalomu alaykum!\nWiKipedia-uz'ga Hush kelibsiz.\n\nSiz o'zingizga qiziq bo'lgan mavzuni yozing va biz uni topishga harakat qilamiz!")


@dp.message_handler()
async def send_wiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi.\nBoshqa nom bilan harakat qilib ko'ring.")

    # old style:
    # await bot.send_message(message.chat.id, message.text)

    # await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
