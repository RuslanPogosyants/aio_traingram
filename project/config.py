import os
import dotenv
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

dotenv.load_dotenv()

gigachat_token = os.getenv("gigachat_token")

bot_token = os.getenv("bot_token")
dp = Dispatcher()
bot = Bot(bot_token, parse_mode=ParseMode.HTML)

db_url = os.getenv("database_url")

