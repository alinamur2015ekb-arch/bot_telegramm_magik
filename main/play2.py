import random
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters import Command
from .keyboard import quest, choice, a, b
from aiogram.enums import ParseMode

router = Router()


@router.message(Command("quest"))  
async def wuest(message: Message):
    await message.answer("Это игра Камень-Ножницы-Бумага. Сделайте выбор.", reply_markup=quest)


# Игра 3
@router.callback_query(F.data == "stone")
async def play_stone(callback: CallbackQuery):
    await play_game(callback, "stone")


@router.callback_query(F.data == "scissors")
async def play_scissors(callback: CallbackQuery):
    await play_game(callback, "scissors")


@router.callback_query(F.data == "paper")
async def play_paper(callback: CallbackQuery):
    await play_game(callback, "paper")


async def play_game(callback: CallbackQuery, user_choice: str):
    choices = ["stone", "scissors", "paper"]
    bot_choice = random.choice(choices)

    smiles = {"stone": "🪨 Камень", "scissors": "✂️ Ножницы", "paper": "📄 Бумага"}

    result = ""
    if user_choice == bot_choice:
        result = "Ничья"
    elif (user_choice == "stone" and bot_choice == "scissors") or \
         (user_choice == "scissors" and bot_choice == "paper") or \
         (user_choice == "paper" and bot_choice == "stone"):
        result = "Ты выиграл"
    else:
        result = "Ты проиграл"

    await callback.message.answer(
        f"Твой выбор: {smiles[user_choice]}\n"
        f"Выбор бота: {smiles[bot_choice]}\n\n"
        f"{result}\n\n"
        f"Сыграем еще? Сделай выбор на кнопках выше!",
    )

    await callback.answer()


# Игра 4
@router.message(Command("player"))
async def player(message: Message):
    await message.answer("Это страшный квест, подтвердите согласие на участие", reply_markup=choice)


@router.callback_query(F.data == "yes")
async def yes(callback: CallbackQuery): 
    photo1 = FSInputFile("scary_photos/scary1.jpg")
    await callback.message.answer_photo(photo1, caption="Страшный квест\n\n<b>Проклятый номер</b>", parse_mode=ParseMode.HTML)
    await callback.message.answer(
        "Вы с подругами решили устроить девичник\n"
        "Твоя подруга Лиза и твоя вторая подруга Кира, она пришла с младшей сестрой Машей\n"
        "Когда вы уже собирались ложиться спать, Маша вдруг предложила поиграть в игру: позвонить на проклятый номер 666.\n\n"
        "Что ты сделаешь?",
        reply_markup=a
    )
    await callback.answer()


@router.callback_query(F.data == "player_a1")
async def player_a1(callback: CallbackQuery):
    photo2 = FSInputFile("scary_photos/scary2.jpg") 
    photo3 = FSInputFile("scary_photos/scary3.jpg")
    
    await callback.message.answer(
        "Давайте определим кто будет звонить считалочкой\n"
        "Эники-Бэники ели вареники, Эники-Бэники бац\n"
        "Считалочка остановилась на тебе\n"
        "Ты позвонила по номеру - абонент временно недоступен\n"
        "Прошло 15 минут\n"
        "Затем вдруг позвонил этот номер"
    )
    await callback.message.answer_photo(photo2, caption="📞 кап кап капля крови")
    await callback.message.answer("<i>Звонок ты ставила на громкую связь</i>\nВсе подумали что это пранк, но ты похолодела\nЛиза предложила лечь спать")
    await callback.message.answer("Ночью вдруг задергалась ручка от двери")
    await callback.message.answer_photo(photo3, caption="А-А-А-А-А")
    await callback.message.answer(
        "<i>Ты пропала без вести</i>\n"
        "Твои подруги попытались тебя спасти, но они тоже пропали.\n"
        "<b>Конец</b>",
        parse_mode=ParseMode.HTML
    )


@router.callback_query(F.data == "player_b1")
async def player_b1(callback: CallbackQuery):
    photo2 = FSInputFile("scary_photos/scary2.jpg")  
    photo3 = FSInputFile("scary_photos/scary3.jpg")
    
    await callback.message.answer(
        "Ну ладно, тогда позвоню я - сказала Маша\n"
        "📞 Номер временно недоступен\n"
        "Через 5 минут"
    )
    await callback.message.answer_photo(photo2, caption="📞 кап кап капля крови")
    await callback.message.answer("<i>Звонок Маша поставила на громкую связь</i>\nВсе подумали что это пранк, но ты похолодела\nЛиза предложила лечь спать")
    await callback.message.answer("Ночью вдруг задергалась ручка от двери")
    await callback.message.answer_photo(photo3, caption="А-А-А-А-А")
    await callback.message.answer(
        "На утро вы проснулись, а Маши негде не было\n"
        "Вы решили что она вас разыграла и Кира позвонила домой, но она сказала что никакой дочерь Маши у нее никогда не было\n"
        "Когда вы пришли в полицию, там сказали что такой девочки никогда не было"
    )
    await callback.message.answer(
        "Лиза предложила тоже позвонить на этот номер\n"
        "Что ты сделаешь?",
        reply_markup=b
    )


@router.callback_query(F.data == "player_a2")
async def player_a2(callback: CallbackQuery):  
    await callback.message.answer("Лиза - ладно ладно")
    await callback.message.answer(
        "Вы выжили, но Маша пропала и все, даже ты, забыли её\n"
        "<b>Конец</b>"
    )


@router.callback_query(F.data == "player_b2")
async def player_b2(callback: CallbackQuery):
    photo3 = FSInputFile("scary_photos/scary3.jpg")
    await callback.message.answer_photo(photo3, caption="На следующую ночь вы все пропали\n<b>Конец</b>")


@router.callback_query(F.data == "no")
async def no(callback: CallbackQuery):
    await callback.message.answer(
        "<b>Команды</b>\n\n"
        "Образовательные функции:\n\n"
        "/mathematics\n/python\n/robotics\n\n"
        "Развлекательные функции:\n"
        "/random\n/funny_photos\n/mems\n/quest\n/player\n\n"
        "Статистика:\n/my_education\n/my_play",
        parse_mode=ParseMode.HTML
    )
    await callback.answer()
