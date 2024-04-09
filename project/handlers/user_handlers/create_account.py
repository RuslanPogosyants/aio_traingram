from project.database.models import User
from aiogram import Dispatcher, F
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, BufferedInputFile
from aiogram.utils.keyboard import InlineKeyboardButton, KeyboardBuilder
from project.config import bot
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.utils.markdown import hbold

from project.database.train_db.splits import split_list


def create_ik(args: str | list) -> InlineKeyboardMarkup:
    builder = KeyboardBuilder(button_type=InlineKeyboardButton)
    if isinstance(args, list):
        for arg in args:
            inline_button = InlineKeyboardButton(text=arg, callback_data=arg)
            builder.add(inline_button)
    else:
        inline_button = InlineKeyboardButton(text=args, callback_data=args)
        builder.add(inline_button)

    markup = InlineKeyboardMarkup(inline_keyboard=builder.export())
    return markup


class UserStates(StatesGroup):
    set_name = State()
    set_age = State()
    set_gender = State()
    set_weight = State()
    set_height = State()
    set_pace = State()
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

    data = await state.get_data()
    bot_message = await bot.edit_message_text(chat_id=callback.from_user.id, text=text,  message_id=data['message_id'])
    await state.update_data(message_id=bot_message.message_id)

    await state.set_state(UserStates.set_name)


async def set_name_ask_age(message: Message, state: FSMContext) -> None:
    user_id = message.from_user.id
    name = message.text
    User.set_name(user_id=user_id, name=name)

    text = f'Ваше имя: {User.get_name(user_id)}\nВведите ваш возраст:'

    data = await state.get_data()
    bot_message = await bot.edit_message_text(chat_id=message.from_user.id, text=text, message_id=data['message_id'])
    await state.update_data(message_id=bot_message.message_id)

    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    await state.set_state(UserStates.set_age)

async def set_age_ask_gender(message: Message, state: FSMContext) -> None:
    user_id = message.from_user.id
    age = message.text
    User.set_age(user_id=user_id, age=int(age))

    text = f'Ваше имя: {User.get_name(user_id)}\nВаш возраст: {User.get_age(user_id)}\nВыберите пол:'

    data = await state.get_data()
    bot_message = await bot.edit_message_text(chat_id=message.from_user.id, text=text, message_id=data['message_id'], reply_markup=create_ik(['Мужской', 'Женский']))
    await state.update_data(message_id=bot_message.message_id)

    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    await state.set_state(UserStates.set_gender)


async def set_gender_ask_height(callback: CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id
    gender = callback.data
    User.set_gender(user_id=user_id, gender=gender)

    text = f'Ваше имя: {User.get_name(user_id)}\nВаш возраст: {User.get_age(user_id)}\nВаш пол: {User.get_gender(user_id)}\nВведите ваш рост:'

    data = await state.get_data()
    bot_message = await bot.edit_message_text(chat_id=callback.from_user.id, text=text,  message_id=data['message_id'])
    await state.update_data(message_id=bot_message.message_id)

    await state.set_state(UserStates.set_height)


async def set_height_ask_weight(message: Message, state: FSMContext) -> None:
    user_id = message.from_user.id
    height = message.text
    User.set_height(user_id=user_id, height=height)

    text = f'Ваше имя: {User.get_name(user_id)}\nВаш возраст: {User.get_age(user_id)}\nВаш пол: {User.get_gender(user_id)}\nВведите ваш рост: {User.get_height(user_id)}\nВведите ваш вес:'

    data = await state.get_data()
    bot_message = await bot.edit_message_text(chat_id=message.from_user.id, text=text, message_id=data['message_id'])
    await state.update_data(message_id=bot_message.message_id)

    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    await state.set_state(UserStates.set_weight)


async def set_weight_ask_pace(message: Message, state: FSMContext) -> None:
    user_id = message.from_user.id
    weight = message.text
    User.set_weight(user_id=user_id, weight=weight)

    text = f'Ваше имя: {User.get_name(user_id)}\nВаш возраст: {User.get_age(user_id)}\nВаш пол: {User.get_gender(user_id)}\nВведите ваш рост: {User.get_height(user_id)}\nВаш вес: {User.get_weight(user_id)}\nВыберите темп:' + '\nP.S. Темп - условное определение нагрузок, т.е. кол-во повторений и подходов, сложность упражнений, каллоража и т.д.'

    data = await state.get_data()
    bot_message = await bot.edit_message_text(chat_id=message.from_user.id, text=text, message_id=data['message_id'], reply_markup=create_ik(['Минимальный', 'Средний', 'Максимальный']))
    await state.update_data(message_id=bot_message.message_id)

    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    await state.set_state(UserStates.set_pace)


async def set_pace_ask_splits(callback: CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id
    pace = callback.data
    User.set_pace(user_id=user_id, pace=pace)

    text = f'Ваше имя: {User.get_name(user_id)}\nВаш возраст: {User.get_age(user_id)}\nВаш пол: {User.get_gender(user_id)}\nВведите ваш рост: {User.get_height(user_id)}\nВаш вес: {User.get_weight(user_id)}\nВаш темп: {User.get_pace(user_id)}\nВыберите один из планов тренировок:'

    data = await state.get_data()
    bot_message = await bot.edit_message_text(chat_id=callback.from_user.id, text=text, message_id=data['message_id'])
    await state.update_data(message_id=bot_message.message_id)

    for split in split_list:
        split_message = await bot.send_photo(chat_id=callback.from_user.id, photo=BufferedInputFile(file=split.photo_in_bytes, filename='PPL.jpg'), caption=f'{split.name} - {split.description}', reply_markup=create_ik(split.name))

    await state.set_state(UserStates.set_split)


async def set_splits_end_create_profile(callback: CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id
    split_name = callback.data
    User.set_split(user_id=user_id, split_name='split.name')

    text = User.view_info(user_id=user_id) + 'Если вы хотите узнать что-то у ИИ, то напишите запрос, начиная с ai'

    data = await state.get_data()
    bot_message = await bot.edit_message_text(chat_id=callback.from_user.id, text=text, message_id=data['message_id'])

    #  await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
    await state.update_data(message_id=bot_message.message_id)
    await state.clear()


def register_handlers_account(dp: Dispatcher) -> None:
    dp.message.register(start, Command('start'))
    dp.callback_query.register(ask_name, lambda callback_query: callback_query.data == 'Начать регистрацию!')
    dp.message.register(set_name_ask_age, UserStates.set_name, lambda x: x.text.isalpha())
    dp.message.register(set_age_ask_gender, UserStates.set_age, lambda x: x.text.isdigit())
    dp.callback_query.register(set_gender_ask_height, UserStates.set_gender, lambda callback_query: callback_query.data in ['Мужской', 'Женский'])
    dp.message.register(set_height_ask_weight, UserStates.set_height, lambda x: x.text.isdigit())
    dp.message.register(set_weight_ask_pace, UserStates.set_weight, lambda x: x.text.isdigit())
    dp.callback_query.register(set_pace_ask_splits, UserStates.set_pace, lambda callback_query: callback_query.data in ['Минимальный', 'Средний', 'Максимальный'])
    dp.message.register(set_splits_end_create_profile, UserStates.set_split, lambda callback_query: callback_query.data in [split.name for split in split_list])
