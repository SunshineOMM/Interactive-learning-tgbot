from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, ContentType
import keyboards as kb

bot = Bot(token=os.environ['BOT_TOKEN'])
dp = Dispatcher(bot)




@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!",reply_markup=kb.create_start_course)

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)

@dp.callback_query_handler(lambda c: c.data == 'create_course')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Прикрепите файл в формате JSON')

@dp.message_handler(content_types=ContentType.DOCUMENT)
async def process_callback_button1(message: types.Message):
    await message.document.download(
       destination_file=f"documents/{message.document.file_unique_id}.json",
    )
    await message.reply( f'Файл принят успешно!')
    await message.reply(message.document)

if __name__ == '__main__':
    executor.start_polling(dp)