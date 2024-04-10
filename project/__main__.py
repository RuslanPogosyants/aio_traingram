from project.handlers.user_handlers.create_account import register_handlers_account
from handlers.jokes_handlers.joke import register_handlers_joke
from handlers.user_handlers.user import register_handlers_user
from handlers.ai_handlers.ai import register_handlers_ai
from config import dp, bot
import asyncio
import logging


async def main() -> None:
    register_handlers_account(dp)
    register_handlers_user(dp)
    register_handlers_joke(dp)
    register_handlers_ai(dp)
    print(await bot.get_webhook_info())
    #####
    # schedule_thread = threading.Thread(target=schedule_loop)
    # schedule_thread.start()
    # asyncio.create_task(notify_periodically())
    #####
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types(), close_bot_session=True)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main())
