import datetime

from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from database.bot_db import sql_command_all_id
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.date import DateTrigger
from config import bot, ADMINS


async def go_to_sleep(bot: Bot):
    user_ids = await sql_command_all_id()
    for user_id in user_ids:
        await bot.send_message(user_id[0], "Иди спать!")


async def wake_up(bot: Bot):
    video = open("media/video.mp4", "rb")
    await bot.send_video(ADMINS[0], video=video)


async def send_message_date(bot: Bot):
    await bot.send_message(ADMINS[0], "DATE TRIGGER!")


async def set_scheduler():
    scheduler = AsyncIOScheduler(timezone='Asia/Bishkek')
    # scheduler.add_job(
    #     go_to_sleep,
    #     trigger=CronTrigger(
    #         hour=datetime.datetime.now().hour,
    #         minute=datetime.datetime.now().minute + 1,
    #         start_date=datetime.datetime.now()
    #     ),
    #     kwargs={"bot": bot},
    # )
    #
    # scheduler.add_job(
    #     wake_up,
    #     trigger=IntervalTrigger(
    #         seconds=60
    #     ),
    #     kwargs={"bot": bot},
    # )

    scheduler.add_job(
        wake_up,
        trigger=DateTrigger(
            # run_date=datetime.datetime(year=2023, month=3, day=23, hour=19, minute=36)
            run_date=datetime.datetime.now() + datetime.timedelta(minutes=1)
        ),
        kwargs={"bot": bot},
    )

    scheduler.start()
