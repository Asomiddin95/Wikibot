1
"""
 2This is a echo bot.
 3It echoes any incoming text messages.
 4"""
import logging
import wikipedia
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '1931131493:AAHdkrXVgpz04COQwqO3N-eM7uH9ZD6h9bI'
wikipedia.set_lang('uz')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
23    This handler will be called when user sends `/start` or `/help` command
24    """
    await message.reply("Assalomu Aleykum")


@dp.message_handler()
async def wiki(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    try:
        m = wikipedia.summary(message.text)
        await message.answer(m)
    except:
        await message.answer("Bu mavzuga oid maqola toplmadi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
