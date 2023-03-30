from aiogram import types, Dispatcher
from .loader import download_video

async def delete_sticker(message: types.Message):
    await message.delete()


# @dp.message_handler()
async def bad_words_filter(message: types.Message):
    if "youtube.com" in message.text:
        await message.answer("Загрузка...")
        video = open(f"../{download_video(message.text)}", "rb")
        await message.answer_video(video)
        await message.answer("Готово!")


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(bad_words_filter, content_types=['text'])
    dp.register_message_handler(delete_sticker, content_types=['sticker', 'photo',
                                                               'animation'])
