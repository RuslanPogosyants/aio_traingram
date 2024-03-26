import dotenv
import os
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

dotenv.load_dotenv()

gigachat_token = os.getenv("GIGACHAT_TOKEN")

TOKEN = os.getenv("BOT_TOKEN")
dp = Dispatcher()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

db_url = os.getenv("DATABASE_URL")
