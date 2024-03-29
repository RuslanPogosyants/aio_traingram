from aiogram.filters import Command
from aiogram.methods import SendMessage
from aiogram import Dispatcher
from aiogram.types import Message
from project.database.models import User


async def user_info(message: Message) -> SendMessage:
    user_id = message.from_user.id
    text = User.view_info(user_id)
    await message.answer(text=text)


async def del_account(message: Message) -> SendMessage:
    user_id = message.from_user.id
    result = User.delete_user(user_id)
    await message.answer(text=result)


def register_handlers_user(dp: Dispatcher):
    dp.message.register(user_info, Command(commands=['profile']))
    dp.message.register(del_account, Command(commands=['del_account']))
