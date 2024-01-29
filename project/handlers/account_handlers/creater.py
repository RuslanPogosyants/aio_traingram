from aiogram.filters import CommandStart
from project.database.models import User
from aiogram import Dispatcher
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardButton, KeyboardBuilder
from project.config import bot
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.utils.markdown import hbold


def create_ik(*args, **kwargs) -> InlineKeyboardMarkup:
    builder = KeyboardBuilder(button_type=InlineKeyboardButton)
    for i in list(*args, **kwargs):
        inline_button = InlineKeyboardButton(text=i, callback_data=i)
        builder.add(inline_button)
    markup = InlineKeyboardMarkup(inline_keyboard=builder.export())
    return markup


class UserStates(StatesGroup):
    ask_name = State()
    set_name = State()
    ask_age = State()
    set_age = State()
    ask_gender = State()
    set_gender = State()
    ask_weight = State()
    set_weight = State()
    ask_height = State()
    set_height = State()
    ask_pace = State()
    set_pace = State()


async def start(message: Message, state: FSMContext) -> None:
    user_id = message.from_user.id
    name = message.from_user.full_name
    await message.answer(f"{hbold(name)}, добро пожаловать!\nВас приветствует {hbold('WorkoutBot!')}")
    if User.user_exist(user_id):
        await message.answer('Вы уже зарегистрированы!')
    else:
        User.create_user(user_id)
        await message.answer('Давайте зарегистрируем вас!')
        await state.set_state(UserStates.ask_name)


async def ask_name(message: Message, state: FSMContext) -> None:
    text = 'Введите ваше имя:'
    await message.answer(text=text)
    await state.set_state(UserStates.set_name)
    bot_message = await bot.send_message(chat_id=message.from_user.id, text=text)
    await state.update_data(message_id=bot_message.message_id)


async def set_name(message: Message, state: FSMContext) -> None:
    user_id = message.from_user.id
    name = message.text
    User.set_name(user_id=user_id, name=name)
    await message.edit_text(text=f'Ваше имя: {hbold(name)}\n'
                                 f'Ваш возраст: {hbold("...")}\n'
                                 f'Ваш пол: {hbold("...")}\n'
                                 f'Ваш вес: {hbold("...")}\n'
                                 f'Ваш рост: {hbold("...")}\n'
                                 f'Ваша цель: {hbold("...")}\n')
    await state.set_state(UserStates.ask_age)


async def set_age(message: Message, state: FSMContext) -> None:
    user_id = message.from_user.id
    age = message.text
    User.set_name(user_id=user_id, age=age)
    await state.set_state(UserStates.ask_gender)


async def ask_gender(callback: CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id
    text = 'Выберите пол:'
    ik_gender = create_ik('Мужской', 'Женский')
    await bot.send_message(chat_id=user_id, text=text, reply_markup=ik_gender)


async def set_gender(callback: CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id
    gender = callback.data
    User.set_gender(user_id=user_id, gender=gender)


async def ask_height(message: Message, state: FSMContext) -> None:
    text = 'Введите рост:'
    await message.answer(text=text)


async def set_height(message:Message, state: FSMContext) -> None:
    user_id = message.from_user.id
    height = message.text
    User.set_height(user_id=user_id, height=height)


async def ask_weight(message: Message, state: FSMContext) -> None:
    text = 'Введите вес:'
    await message.answer(text=text)


async def set_weight(message: Message, state: FSMContext) -> None:
    user_id = message.from_user.id
    weight = message.text
    User.set_weight(user_id=user_id, weight=weight)


async def ask_pace(message: Message, state: FSMContext) -> None:
    text = 'Выберите темп:'
    await message.answer(text=text)


async def set_pace(callback: CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id
    pace = callback.data
    User.set_pace(user_id=user_id, pace=pace)


def register_handlers_account(dp: Dispatcher):
    dp.message.register(start)
    dp.message.register(ask_name, UserStates.ask_name)
    dp.message.register(set_name, UserStates.set_name)
