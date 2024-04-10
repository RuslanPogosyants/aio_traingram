from project.database.models import User
from project.config import bot
import schedule
import datetime
import asyncio
import time


async def notify_periodically():
    now = datetime.datetime.now().time()

    desired_time = datetime.time(7, 00, 0)

    time_difference = (datetime.datetime.combine(datetime.date.today(), desired_time) -
                       datetime.datetime.combine(datetime.date.today(), now))

    if time_difference.total_seconds() < 0:
        time_difference += datetime.timedelta(seconds=1)

    await asyncio.sleep(time_difference.total_seconds())


async def notify():
    for user_id, user in users.items():
        SplitName = user.current_split
        Splits = load_splits_from_json(splits_file_path)
        TrainDays: list = Splits[SplitName].listOfSessions
        text = f"{Splits[SplitName].numberOfsessions[str(user.last_day_sent)]:-^60}\n"
        for x in TrainDays[user.last_day_sent]:
            text += str(x)
        user.last_day_sent = (user.last_day_sent + 1) % len(TrainDays)
        users[user_id] = user
        save_users_data(users, users_file_path)
        await bot.send_message(chat_id=user_id, text=text, parse_mode='Markdown', disable_web_page_preview=True)


#  Запуск планировщика/обнуление каллорий по времени
def schedule_loop():
    while True:
        # Запускаем планировщик и выполняем отложенные задачи
        schedule.run_pending()
        time.sleep(1)
