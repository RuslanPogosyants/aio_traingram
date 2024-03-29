import sys
import asyncio
import logging
from config import dp, bot
from handlers.user import register_handlers_user
from project.handlers.set_menu import set_main_menu
from handlers.ai_handlers.ai import register_handlers_ai
from handlers.jokes_handlers.joke import register_handlers_joke
from handlers.account_handlers.creater import register_handlers_account


async def main() -> None:
    await set_main_menu(bot)
    register_handlers_user(dp)
    register_handlers_joke(dp)
    register_handlers_ai(dp)
    register_handlers_account(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
