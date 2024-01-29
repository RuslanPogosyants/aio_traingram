import logging
import asyncio
import sys
from handlers.user import register_handlers_user
from handlers.jokes_handlers.joke import register_handlers_joke
from handlers.advices_handlers.advice import register_handlers_advice
from handlers.account_handlers.creater import register_handlers_account
from config import dp, bot


async def main() -> None:
    register_handlers_user(dp)
    register_handlers_joke(dp)
    register_handlers_advice(dp)
    register_handlers_account(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
