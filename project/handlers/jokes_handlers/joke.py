from .parser import jokes
from aiogram import Dispatcher,  F
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardButton, KeyboardBuilder
from random import choice
from project.config import bot


def create_inline_keyboard():
    builder = KeyboardBuilder(button_type=InlineKeyboardButton)
    inline_button_joke = InlineKeyboardButton(text='Шутку!', callback_data='joke')
    builder.add(inline_button_joke)
    markup = InlineKeyboardMarkup(inline_keyboard=builder.export())
    return markup


async def get_joke(message: Message):
    await bot.send_message(message.chat.id, choice(jokes), reply_markup=create_inline_keyboard())


async def edit_get_joke(callback: CallbackQuery):
    await callback.message.edit_text(choice(jokes), reply_markup=create_inline_keyboard())


def register_handlers_joke(dp: Dispatcher):
    dp.message.register(get_joke, F.text.casefold() == '/joke')
    dp.callback_query.register(edit_get_joke, lambda callback_query: callback_query.data == 'joke')
