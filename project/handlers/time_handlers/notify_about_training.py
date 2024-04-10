from project.database.models import User
from project.config import bot
import schedule
import datetime
import asyncio
import time

from project.database.train_db.splits import split_list
from project.handlers.user_handlers.user import what_to_do


async def notify_periodically():
    now = datetime.datetime.now().time()

    desired_time = datetime.time(7, 0, 0)

    time_difference = (datetime.datetime.combine(datetime.date.today(), desired_time) -
                       datetime.datetime.combine(datetime.date.today(), now))

    if time_difference.total_seconds() < 1:
        time_difference += datetime.timedelta(seconds=1)

    await asyncio.sleep(time_difference.total_seconds())

    while True:
        await notify()
        await asyncio.sleep(86400)


async def notify():
    for user in User.__iter__():
        await bot.send_message(chat_id=user.id, text='Твой план на сегодня!')
        day_index = User.get_last_day_sent(user_id=user.id)
        user_split = User.get_split(user_id=user.id)
        split_as_object = next((split for split in split_list if split.name == user_split), None)
        text = str(split_as_object.days[day_index])
        await bot.send_message(chat_id=user.id, text=text, parse_mode='Markdown', disable_web_page_preview=True)


#  Запуск планировщика/обнуление каллорий по времени
def schedule_loop():
    while True:
        # Запускаем планировщик и выполняем отложенные задачи
        schedule.run_pending()
        time.sleep(1)
