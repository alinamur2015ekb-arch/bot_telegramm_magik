from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from database import get_answer_by_id, get_play_by_id
from aiogram.enums import ParseMode

router = Router()

@router.message(Command("my_education"))
async def my_education(message: Message):
    user_id = message.from_user.id
    
    answer_data = await get_answer_by_id(user_id)
    if answer_data is None:
        await message.answer(
            "Привет! В базе еще нет твоих результатов по учебе.\n"
            "Пройди сначала викторины по математике, пайтону или робототехнике!"
        )
        return

    math1 = answer_data[1] if answer_data[1] is not None else 0
    math2 = answer_data[2] if answer_data[2] is not None else 0
    math3 = answer_data[3] if answer_data[3] is not None else 0

    py1 = answer_data[4] if answer_data[4] is not None else 0
    py2 = answer_data[5] if answer_data[5] is not None else 0
    py3 = answer_data[6] if answer_data[6] is not None else 0

    rob1 = answer_data[7] if answer_data[7] is not None else 0
    rob2 = answer_data[8] if answer_data[8] is not None else 0

    await message.answer(
        f"📊 **ТВОЯ УЧЕБА:**\n\n"
        f"🧠 **Математика:**\n"
        f" ├ 1 уровень: {math1}/5\n"
        f" ├ 2 уровень: {math2}/5\n"
        f" └ 3 уровень: {math3}/5\n\n"
        f"🐍 **Python:**\n"
        f" ├ 1 уровень: {py1}/5\n"
        f" ├ 2 уровень: {py2}/5\n"
        f" └ 3 уровень: {py3}/5\n\n"
        f"🤖 **Робототехника:**\n"
        f" ├ 1 уровень: {rob1}/3\n"
        f" └ 2 уровень: {rob2}/3",
        parse_mode=ParseMode.MarkdownV2 
    )


@router.message(Command("my_play"))
async def my_play(message: Message):
    user_id = message.from_user.id
    
    play_data = await get_play_by_id(user_id)
    
    if play_data is None:
        await message.answer(
            "Привет! 👋 Ты еще не играла в игры нашего бота.\n"
            "Запусти /random или пройди квест, чтобы занести результаты в базу!"
        )
        return

    random_game = play_data[1] if play_data[1] is not None else 0  
    meme_game = play_data[2] if play_data[2] is not None else 0

    await message.answer(
        f"🎮 <b>ТВОИ ИГРЫ:</b>\n\n"
        f"🎲 <b>Угадай число:</b> {random_game} попыток(ки)\n"
        f"<b>Викторина по мемам:</b> {meme_game}/5",
        parse_mode=ParseMode.HTML
    )
