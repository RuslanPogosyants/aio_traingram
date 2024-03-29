from .api import request_answer
from aiogram import Dispatcher,  F
from aiogram.types import Message
from project.config import bot


async def ai_answer(message: Message):
    user_id = message.from_user.id
    text = message.text[3:]
    await bot.send_message(chat_id=user_id, text=request_answer(promt=text))


def register_handlers_ai(dp: Dispatcher):
    dp.message.register(ai_answer, lambda message: message.text.startswith('ai'))
