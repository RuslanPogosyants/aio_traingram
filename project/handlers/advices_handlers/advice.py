from aiogram import Dispatcher,  F
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardButton, KeyboardBuilder
from random import choice
from project.config import bot


def create_builder_next_back():
    builder = KeyboardBuilder(button_type=InlineKeyboardButton)
    ib_navigation = [InlineKeyboardButton(text='Назад', callback_data='back'), InlineKeyboardButton(text='Далее', callback_data='next')]
    builder.add(*ib_navigation)
    return builder


async def main_advices(message: Message) -> None:
    user_id = message.from_user.id
    builder = create_builder_next_back()
    builder.add(InlineKeyboardButton(text='категория', callback_data='back'))
    ik_category_advice = InlineKeyboardMarkup(inline_keyboard=builder.export())
    text = 'Выберите категорию:'
    await bot.send_message(chat_id=user_id, text=text, reply_markup=ik_category_advice)


def register_handlers_advice(dp: Dispatcher):
    dp.message.register(main_advices, F.text.casefold() == 'advice')
