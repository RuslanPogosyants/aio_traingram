from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.methods import SendMessage
from aiogram import Dispatcher
from aiogram.types import Message, BufferedInputFile, CallbackQuery
from project.config import bot
from project.database.models import User
from project.database.train_db.splits import split_list
from project.handlers.user_handlers.create_account import create_ik
from aiogram.fsm.state import StatesGroup, State


class ChangeSplit(StatesGroup):
    change_split = State()


async def user_info(message: Message) -> SendMessage:
    user_id = message.from_user.id
    text = User.view_info(user_id)
    await message.answer(text=text)


async def del_account(message: Message) -> SendMessage:
    user_id = message.from_user.id
    text = User.delete_user(user_id)
    await message.answer(text=text)


async def change_split(message: Message, state: FSMContext) -> SendMessage:
    split_message_ids = []
    for split in split_list:
        split_message = await bot.send_photo(chat_id=message.from_user.id, photo=BufferedInputFile(file=split.photo_in_bytes, filename='PPL.jpg'), caption=f'{split.name} - {split.description}', reply_markup=create_ik(split.name))
        split_message_ids.append(split_message.message_id)

    await state.update_data(split_message_ids=split_message_ids)
    await state.set_state(ChangeSplit.change_split)


async def remove_split(callback: CallbackQuery, state: FSMContext) -> SendMessage:
    user_id = callback.from_user.id
    text = User.view_info(user_id=user_id)
    data = await state.get_data()
    split_message_ids = data.get('split_message_ids', [])
    for message_id in split_message_ids:
        await bot.delete_message(chat_id=user_id, message_id=message_id)

    await bot.send_message(chat_id=user_id, text=text)
    await state.clear()


def register_handlers_user(dp: Dispatcher):
    dp.message.register(user_info, Command(commands=['profile']))
    dp.message.register(del_account, Command(commands=['del_account']))
    dp.message.register(change_split, Command(commands=['changesplit']))
    dp.callback_query.register(remove_split, ChangeSplit.change_split, lambda callback_query: callback_query.data in [split.name for split in split_list])
