from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from .keyboard import robotics
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from state.state import robotics1, robotics2
from database import create_answer

router = Router()
one_robotics_answer = ["2", "1", "3"]
two_robotics_answer = ["2", "1", "2"]


@router.message(Command("robotics"))
async def robotics(message: Message):  
    await message.answer("Выберите уровень сложности",
                         reply_markup=robotics)


# 1 уровень
@router.callback_query(F.data == "one_robotics")
async def one_robotics(callback: CallbackQuery, state: FSMContext): 
    await callback.message.answer(
        "Робототехника на arduino. <b>Уровень Легкий.</b> Писать только номер ответа\n\n"
        "1 вопрос: Где пишется код для arduino?\n"
        "1.) В текстовом редакторе\n"
        "2.) В Arduino IDE\n"
        "3.) В компиляторе",
        parse_mode="HTML"
    )
    await state.set_state(robotics1.a)
    await callback.answer()


@router.message(robotics1.a) 
async def a6(message: Message, state: FSMContext):  
   
    await state.set_data({"a": message.text})
    
    await message.answer(
        "2 вопрос: Как называется код в arduino IDE?\n"
        "1.) Скетч\n"
        "2.) Кодот\n"
        "3.) Arduino"
    )
    await state.set_state(robotics1.b)


@router.message(robotics1.b)
async def b6(message: Message, state: FSMContext):
    await state.set_data({"b": message.text})
    
    await message.answer(
        "3 вопрос: Какие 2 функции обязательны в коде для arduino IDE?\n"
        "1.) vood(), loop()\n"
        "2.) setup(), lood()\n"
        "3.) setup(), loop()"
    )
    await state.set_state(robotics1.c)


@router.message(robotics1.c)
async def c6(message: Message, state: FSMContext):
    await state.set_data({"c": message.text})
    
    one_count_robotics = 0
    data = await state.get_data()
    
    a = data.get("a")
    b = data.get("b")
    c = data.get("c")
    
    if a and a.strip() == one_robotics_answer[0]:
        one_count_robotics += 1
    if b and b.strip() == one_robotics_answer[1]:
        one_count_robotics += 1
    if c and c.strip() == one_robotics_answer[2]:
        one_count_robotics += 1
    
    await message.answer(f"У вас {one_count_robotics}/3 <b>правильных</b> ответов", parse_mode="HTML")
    
    await create_answer(answer_robotics1=one_count_robotics)
    await state.clear()


# 2 уровень
@router.callback_query(F.data == "two_robotics")
async def two_robotics(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(
        "Робототехника на arduino\n\n"
        "Уровень 2 - <b>Сложный</b>\n\n"
        "1 вопрос: Какой пин у встроенного светодиода в плате arduino uno?\n"
        "1.) 12\n"
        "2.) 13\n"
        "3.) 11",
        parse_mode="HTML"
    )
    await state.set_state(robotics2.a)
    await callback.answer()


@router.message(robotics2.a)
async def a7(message: Message, state: FSMContext):
    await state.set_data({"a": message.text})
    
    await message.answer(
        "2 вопрос: Как в коде прописать паузу в Arduino IDE?\n"
        "1.) delay\n"
        "2.) pause\n"
        "3.) stop"
    )
    await state.set_state(robotics2.b)


@router.message(robotics2.b)
async def b7(message: Message, state: FSMContext):
    await state.set_data({"b": message.text})
    
    await message.answer(
        "3 вопрос: Какое напряжение обычно в плате arduino?\n"
        "1.) 13V\n"
        "2.) 5V\n"
        "3.) 220V"
    )
    await state.set_state(robotics2.c)


@router.message(robotics2.c)
async def c7(message: Message, state: FSMContext):
    await state.set_data({"c": message.text})
    
    two_count_robotics = 0
    data = await state.get_data()
    
    a = data.get("a")
    b = data.get("b")
    c = data.get("c")
    
    if a and a.strip() == two_robotics_answer[0]:
        two_count_robotics += 1
    if b and b.strip() == two_robotics_answer[1]:
        two_count_robotics += 1
    if c and c.strip() == two_robotics_answer[2]:
        two_count_robotics += 1
    
    await message.answer(f"У вас {two_count_robotics}/3 <b>правильных</b> ответов", parse_mode="HTML")
    
    await create_answer(answer_robotics2=two_count_robotics)
    await state.clear()