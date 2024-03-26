from aiogram.filters import CommandStart
from project.database.models import User
from aiogram import Dispatcher, F
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardButton, KeyboardBuilder
from project.config import bot
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.utils.markdown import hbold


def create_ik(arg) -> InlineKeyboardMarkup:
    builder = KeyboardBuilder(button_type=InlineKeyboardButton)
    inline_button = InlineKeyboardButton(text=arg, callback_data=arg)
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
    ask_splits = State()
    set_split = State()


async def start(message: Message, state: FSMContext) -> None:
    user_id = message.from_user.id
    name = message.from_user.full_name
    await message.answer(f"{hbold(name)}, добро пожаловать!\nВас приветствует {hbold('WorkoutBot!')}")
    if User.user_exist(user_id):
        await message.answer('Вы уже зарегистрированы!')
    else:
        User.create_user(user_id)
        bot_message = await bot.send_message(chat_id=user_id, text='Давайте зарегистрируем вас!', reply_markup=create_ik('Начать регистрацию!'))
        await state.update_data(message_id=bot_message.message_id)


async def ask_name(callback: CallbackQuery, state: FSMContext) -> None:
    text = 'Введите ваше имя:'
    await state.set_state(UserStates.set_name)
    data = await state.get_data()
    bot_message = await bot.edit_message_text(chat_id=callback.from_user.id, text=text,  message_id=data['message_id'])
    await state.update_data(message_id=bot_message.message_id)


async def set_name(message: Message, state: FSMContext) -> None:
    user_id = message.from_user.id
    name = message.text
    User.set_name(user_id=user_id, name=name)
    text = f'Ваше имя {User.name}/nВведите ваш возраст:'
    data = await state.get_data()
    bot_message = await bot.edit_message_text(chat_id=message.from_user.id, text=text, message_id=data['message_id'])
    await state.update_data(message_id=bot_message.message_id)
    await state.set_state(UserStates.ask_age)


async def set_age(message: Message, state: FSMContext) -> None:
    user_id = message.from_user.id
    age = message.text
    User.set_age(user_id=user_id, age=age)
    await state.set_state(UserStates.ask_gender)


async def ask_gender(callback: CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id
    text = 'Выберите пол:'
    ik_gender = create_ik('Мужской', 'Женский')
    await bot.send_message(chat_id=user_id, text=text, reply_markup=ik_gender)
    await state.set_state(UserStates.set_gender)


async def set_gender(callback: CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id
    gender = callback.data
    User.set_gender(user_id=user_id, gender=gender)
    await state.set_state(UserStates.ask_height)


async def ask_height(message: Message, state: FSMContext) -> None:
    text = 'Введите рост:'
    await message.answer(text=text)
    await state.set_state(UserStates.set_height)


async def set_height(message:Message, state: FSMContext) -> None:
    user_id = message.from_user.id
    height = message.text
    User.set_height(user_id=user_id, height=height)
    await state.set_state(UserStates.ask_weight)


async def ask_weight(message: Message, state: FSMContext) -> None:
    text = 'Введите вес:'
    await message.answer(text=text)
    await state.set_state(UserStates.set_weight)


async def set_weight(message: Message, state: FSMContext) -> None:
    user_id = message.from_user.id
    weight = message.text
    User.set_weight(user_id=user_id, weight=weight)
    await state.set_state(UserStates.ask_pace)


async def ask_pace(message: Message, state: FSMContext) -> None:
    text = 'Выберите темп:'
    await message.answer(text=text)
    await state.set_state(UserStates.set_pace)


async def set_pace(callback: CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id
    pace = callback.data
    User.set_pace(user_id=user_id, pace=pace)
    await state.set_state(UserStates.ask_splits)


async def ask_splits(message: Message, state: FSMContext) -> None:
    user_id = message.from_user.id
    text = '...'
    await message.answer(text=text)
    await state.set_state(UserStates.set_split)


async def set_splits(callback: CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id
    User.set_split(user_id, 'split.name')
    text = '...'
    await bot.send_message(chat_id=user_id, text=text)


async def wrong_age(message: Message, state: FSMContext):
    text = 'Возраст должен быть целым числом от 4 до 120.\n\nПопробуйте еще раз\n\n'
    await message.answer(text=text)


async def wrong_name(message: Message, state: FSMContext):
    text = 'Имя не должно содержать символов или цифр.\n\nПопробуйте еще раз\n\n'
    await message.answer(text=text)


async def wrong_height(message: Message, state: FSMContext):
    text = 'Рост должен быть указан в сантиметрах, от 100 до 300.\n\nПожалуйста, введите корректный рост.\n\n'
    await message.answer(text=text)


async def wrong_weight(message: Message, state: FSMContext):
    text = 'Вес должен быть указан в килограммах, от 20 до 300.\n\nПожалуйста, введите корректный вес.\n\n'
    await message.answer(text=text)


def register_handlers_account(dp: Dispatcher):
    dp.message.register(start, F.text.casefold() == '/start')
    dp.callback_query.register(ask_name, lambda callback_query: callback_query.data == 'Начать регистрацию!')
    dp.message.register(set_name, UserStates.set_name, lambda x: x.text.isalpha())


