from aiogram import Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.utils.markdown import hbold
from project.database.models import User
from aiogram import Dispatcher
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardButton, KeyboardBuilder
from project.config import bot


def create_ik(*args, **kwargs) -> InlineKeyboardMarkup:
    builder = KeyboardBuilder(button_type=InlineKeyboardButton)
    for i in list(*args, **kwargs):
        inline_button = InlineKeyboardButton(text=i, callback_data=i)
        builder.add(inline_button)
    markup = InlineKeyboardMarkup(inline_keyboard=builder.export())
    return markup


async def start(message: Message) -> None:
    user_id = message.from_user.id
    name = message.from_user.full_name
    await message.answer(f"{hbold(name)}, добро пожаловать!\nВас приветствует {hbold('WorkoutBot!')}")
    if User.user_exist(user_id):
        await message.answer('Вы уже зарегистрированы!')
    else:
        User.create_user(user_id)


async def ask_age(message: Message) -> None:
    text = 'Введите возраст:'
    await message.answer(text=text)


async def set_age(message: Message) -> None:
    user_id = message.from_user.id
    age = message.text
    User.set_name(user_id=user_id, age=age)


async def ask_gender(callback: CallbackQuery) -> None:
    user_id = callback.from_user.id
    text = 'Выберите пол:'
    ik_gender = create_ik('Мужской', 'Женский')
    await bot.send_message(chat_id=user_id, text=text, reply_markup=ik_gender)


async def set_gender(callback: CallbackQuery) -> None:
    user_id = callback.from_user.id
    gender = callback.data
    User.set_gender(user_id=user_id, gender=gender)


async def ask_height(message: Message) -> None:
    text = 'Введите рост:'
    await message.answer(text=text)


async def set_height(message:Message) -> None:
    user_id = message.from_user.id
    height = message.text
    User.set_height(user_id=user_id, height=height)


async def ask_weight(message: Message) -> None:
    text = 'Введите вес:'
    await message.answer(text=text)


async def set_weight(message: Message) -> None:
    user_id = message.from_user.id
    weight = message.text
    User.set_weight(user_id=user_id, weight=weight)


async def ask_pace(message: Message) -> None:
    text = 'Выберите темп:'
    await message.answer(text=text)


async def set_pace(callback: CallbackQuery) -> None:
    user_id = callback.from_user.id
    pace = callback.data
    User.set_pace(user_id=user_id, pace=pace)


async def user_info(message: Message) -> None:
    user_id = message.from_user.id
    text = User.view_info(user_id=user_id)
    await message.answer(text=text)


async def del_account(message: Message) -> None:
    user_id = message.from_user.id
    if User.user_exist(user_id):
        User.delete_user(user_id)
        await message.answer('Ваш аккаунт успешно удален!')
    else:
        await message.answer('Вы не зарегистрированы!')


def register_handlers_user(dp: Dispatcher):
    dp.message.register(start, CommandStart())

    dp.message.register(del_account, Command(commands=['del_account']))
