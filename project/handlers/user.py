from aiogram import Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.utils.markdown import hbold
from project.database.models import User
from aiogram import Dispatcher
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardButton, KeyboardBuilder
from project.config import bot
from project.database.base import get_session
from project.database.models import User


async def user_info(message: Message) -> None:
    user_id = message.from_user.id
    text = User.view_info(user_id)
    await message.answer(text=text)


async def del_account(message: Message) -> None:
    user_id = message.from_user.id
    result = User.delete_user(user_id)
    await message.answer(text=result)


def register_handlers_user(dp: Dispatcher):
    dp.message.register(user_info, Command(commands=['info']))
    dp.message.register(del_account, Command(commands=['del_account']))
