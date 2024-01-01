import dotenv
import os
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

dotenv.load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
dp = Dispatcher()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

ai_token = os.getenv("AI_TOKEN")
