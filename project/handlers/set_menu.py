from aiogram.types import BotCommand
from aiogram import Bot


menu_dict = {
    'start': '🔁 Старт/рестарт бота',
    'profile': '👤 Показать ваш профиль',
    'joke': '😂 Получить случайную шутку',
    'changesplit': '🔀 Изменить сплит',
    'mysplit': '📊 Показать текущий сплит',
    'training': '🏋️‍♀️ Показать вашу тренировочную таблицу',
    'del_account': '❌ Удалить профиль'
}


async def set_main_menu(bot: Bot):
    main_menu_commands = [BotCommand(
                                command=command,
                                description=description) for command, description in menu_dict.items()]
    await bot.set_my_commands(main_menu_commands)
