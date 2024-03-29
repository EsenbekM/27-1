from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from config import bot
from keyboards.client_kb import start_markup
from database.bot_db import sql_command_random
from parser.films import parser


# @dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Hello world!", reply_markup=start_markup)


# @dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    photo = open('media/cat.jpg', 'rb')
    await message.answer_photo(photo=photo,
                               caption="Сам разбирайся!")
    # await bot.send_photo(
    #     message.from_user.id,
    #     photo=photo,
    #     caption="Сам разбирайся!"
    # )


# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="button_1")
    markup.add(button_1)

    question = "By whom invented Python?"
    answer = [
        "Harry Potter",
        "Putin",
        "Guido Van Rossum",
        "Voldemort",
        "Griffin",
        "Linus Torvalds",
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Стыдно не знать",
        open_period=5,
        reply_markup=markup
    )


async def get_random_user(message: types.Message):
    random_user = await sql_command_random()
    await message.answer_photo(
        photo=random_user[-1],
        caption=f"{random_user[2]} {random_user[3]} {random_user[4]} {random_user[5]}\n"
                f"@{random_user[1]}"
    )


async def get_films(message: types.Message):
    films = parser()
    count = int(message.text.split()[1])
    for film in films:
        count -= 1
        if count == 0:
            break
        await message.answer(
            # f"{film['link']}\n\n"
            f"<b><a href='{film['link']}'>{film['title']}</a></b>\n"
            f"#Y{film['year']}\n"
            f"#{film['genre']}\n"
            f"#{film['country']}\n",
            reply_markup=InlineKeyboardMarkup().add(
                InlineKeyboardButton("СМОТРЕТЬ", url=film['link'])
            ),
            parse_mode=ParseMode.HTML
        )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(help_command, commands=['help'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(get_random_user, commands=['get'])
    dp.register_message_handler(get_films, commands=['films'])
