from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


# keyboards.py
create_start_course = InlineKeyboardMarkup().add(InlineKeyboardButton('Создать курс', callback_data='create_course'),
                                        InlineKeyboardButton('Начать курс', callback_data='start_course'))

