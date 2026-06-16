from aiogram import Router, F
import random
from aiogram.filters import Command
from aiogram.types import Message
from database import create_play
from state.state import play, mems
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile

router = Router()
answers_memes = ["2", "3", "1", "3", "2"]


@router.message(Command("random"))
async def random_game(message: Message, state: FSMContext):  
    number = random.randint(1, 10)
    await state.update_data(
        number=number,
        count_number=1,
        no_count=3 
    )
    await message.answer("Это игра Угадай число от 1 до 10\nУ тебя есть 3 попытки. Введи число")
    await state.set_state(play.random)


# Игра 1
@router.message(play.random, F.text)
async def game_loop(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Введи именно число от 1 до 10")
        return

    user_number = int(message.text)
    data = await state.get_data()
    number = data.get("number")
    count = data.get("count_number")
    no_count = data.get("no_count")

    if user_number == number:
        await message.answer(f"ПОЗДРАВЛЯЮ! Ты угадала число {number} с {count} попытки!")
        await create_play(random=count)  
        await state.clear() 
    else:
        count += 1
        no_count -= 1

        if no_count > 0:
            await message.answer(f"Не угадано\nУ тебя осталось {no_count} попыток. Попробуй еще раз:")
            await state.update_data(count_number=count, no_count=no_count)
        else:
            await message.answer(f"Вы проиграли! Попытки закончились. Было загадано число {number}.\nСыграть заново: /random")
            await state.clear()


# Игра 2
@router.message(Command("mems")) 
async def memes(message: Message, state: FSMContext):
    await message.answer("Йоу это викторина по мемчикам")
    await message.answer("1 вопрос Писать только цифру ответа\nКакая реплика в меме про Галю?\n1.) Галя у нас проблема\n2.) Галя у нас отмена\n3.) Галя у нас возврат")
    await state.update_data({"mems1": None})  
    await state.set_state(mems.mems1)


@router.message(mems.mems1)
async def mems1(message: Message, state: FSMContext):
    await state.update_data({"mems1": message.text}) 
    
    photo1 = FSInputFile("meme_photos/mems1.jpg")
    await message.answer_photo(photo1, caption="2 вопрос\nЧто это за персонаж?\n1.) Ищун\n2.) Пердунчик\n3.) Ждун")
    await state.set_state(mems.mems2)


@router.message(mems.mems2)
async def mems2(message: Message, state: FSMContext):
    await state.update_data({"mems2": message.text})
    
    photo2 = FSInputFile("meme_photos/mems2.jpg")
    await message.answer_photo(photo2, caption="3 вопрос\nКак зовут этого кота?\n1.) Бендер\n2.) Котэ\n3.) Самсон")
    await state.set_state(mems.mems3)


@router.message(mems.mems3)
async def mems3(message: Message, state: FSMContext):
    await state.update_data({"mems3": message.text})
    
    photo3 = FSInputFile("meme_photos/mems3.jpg") 
    await message.answer_photo(photo3, caption="4 вопрос\nКак называют этот мем?\n1.) Недавольный котик\n2.) Злобный кот\n3.) Сердитый код")
    await state.set_state(mems.mems4)


@router.message(mems.mems4)
async def mems4(message: Message, state: FSMContext):
    await state.update_data({"mems4": message.text})
    
    photo4 = FSInputFile("meme_photos/mems4.jpg")
    await message.answer_photo(photo4, caption="5 вопрос\nКак называют этот мем?\n1.) Жалкий хомяк\n2.) Грустный хомяк\n3.) Хитрый хомяк")
    await state.set_state(mems.mems5)


@router.message(mems.mems5)
async def mems5(message: Message, state: FSMContext):
    await state.update_data({"mems5": message.text})
    
    count_mems = 0
    data = await state.get_data()

    mems1 = data.get("mems1")
    mems2 = data.get("mems2")
    mems3 = data.get("mems3")
    mems4 = data.get("mems4")
    mems5 = data.get("mems5")

    if mems1 and mems1.strip() == answers_memes[0]:
        count_mems += 1
    if mems2 and mems2.strip() == answers_memes[1]:
        count_mems += 1
    if mems3 and mems3.strip() == answers_memes[2]:
        count_mems += 1
    if mems4 and mems4.strip() == answers_memes[3]:
        count_mems += 1
    if mems5 and mems5.strip() == answers_memes[4]:
        count_mems += 1

    await message.answer(f"У вас {count_mems}/5 правильных ответов😝")

    await create_play(meme=count_mems)  
    await state.clear()  