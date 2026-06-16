from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from .keyboard import math
from state.state import math1, math2, math3
from aiogram.fsm.context import FSMContext
from database import create_answer

router = Router()
answers_math1 = ["56", "5", "230", "16", "13"]
answers_math2 = ["1/5", "10/2", "5/3", "5/4", "6/4"]
answers_math3 = ["16", "3", "2.5", "15", "3"]


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "<b>Команды</b> \n\n Образовательные функции \n\n /mathematics \n /python \n /robotics "
        "\n\n Развлекательные функции \n /random \n /funny_photos \n /mems \n /quest \n /player \n\n Статистика \n /my_education \n /my_play",
        parse_mode="HTML"
    )


@router.message(Command("mathematics"))
async def mathes(message: Message):
    await message.answer("Выберите уровень сложности", reply_markup=math)


# Уровень 1
@router.callback_query(F.data == "one_math")
async def one(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Викторина по математике уровень легкий")
    await callback.message.answer("<b>1 вопрос</b> \n 8 * 7", parse_mode="HTML")
    await state.set_state(math1.a)
    await callback.answer()


@router.message(math1.a)  # без F.text
async def a(message: Message, state: FSMContext):  # порядок: message, state
    await state.set_data({"a": message.text})  # сохраняем ответ
    
    await message.answer("<b>2 вопрос</b> 45/9", parse_mode="HTML")
    await state.set_state(math1.b)


@router.message(math1.b)
async def b(message: Message, state: FSMContext):
    await state.set_data({"b": message.text})
    
    await message.answer("<b>3 вопрос</b> 23 * 10", parse_mode="HTML")
    await state.set_state(math1.c)


@router.message(math1.c)
async def c(message: Message, state: FSMContext):
    await state.set_data({"c": message.text})
    
    await message.answer("<b>4 вопрос</b> 48/3", parse_mode="HTML")
    await state.set_state(math1.d)


@router.message(math1.d)
async def d(message: Message, state: FSMContext):
    await state.set_data({"d": message.text})
    
    await message.answer("<b>5 вопрос</b> 52/4")
    await state.set_state(math1.e)


@router.message(math1.e)
async def e(message: Message, state: FSMContext):
    await state.set_data({"e": message.text})
    
    count_math1 = 0
    data = await state.get_data()
    
    # Без запятых — чтобы не было tuple
    a = data.get("a")
    b = data.get("b")
    c = data.get("c")
    d = data.get("d")
    e = data.get("e")
    
    # Сравниваем строки (убираем пробелы)
    if a and a.strip() == answers_math1[0]:
        count_math1 += 1
    if b and b.strip() == answers_math1[1]:
        count_math1 += 1
    if c and c.strip() == answers_math1[2]:
        count_math1 += 1
    if d and d.strip() == answers_math1[3]:
        count_math1 += 1
    if e and e.strip() == answers_math1[4]:
        count_math1 += 1
    
    await message.answer(f"У вас {count_math1}/5 <b>правильных</b> ответов.", parse_mode="HTML")
    
    await create_answer(answer_math1=count_math1)
    await state.clear()


# Уровень 2
@router.callback_query(F.data == "two_math")
async def two(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Викторина по математике уровень средний")
    await callback.message.answer("<b>1 вопрос</b> \n Сократи дробь 6/30 до самой маленькой возможной дроби", parse_mode="HTML")
    await state.set_state(math2.a1)
    await callback.answer()


@router.message(math2.a1)
async def a1(message: Message, state: FSMContext):
    await state.set_data({"a1": message.text})
    
    await message.answer("<b>2 вопрос</b> Запиши число 5 дробью с числителем 10", parse_mode="HTML")
    await state.set_state(math2.b1)


@router.message(math2.b1)
async def b1(message: Message, state: FSMContext):
    await state.set_data({"b1": message.text})
    
    await message.answer("<b>3 вопрос</b> 2/3 + 3/3", parse_mode="HTML")
    await state.set_state(math2.c1)


@router.message(math2.c1)
async def c1(message: Message, state: FSMContext):
    await state.set_data({"c1": message.text})
    
    await message.answer("<b>4 вопрос</b> 10/4 - 5/4", parse_mode="HTML")
    await state.set_state(math2.d1)


@router.message(math2.d1)
async def d1(message: Message, state: FSMContext):
    await state.set_data({"d1": message.text})
    
    await message.answer("<b>5 вопрос</b> 2/2 * 3/2")
    await state.set_state(math2.e1)


@router.message(math2.e1)
async def e1(message: Message, state: FSMContext):
    await state.set_data({"e1": message.text})
    
    count_math2 = 0
    data = await state.get_data()
    
    a = data.get("a")
    b = data.get("b")
    c = data.get("c")
    d = data.get("d")
    e = data.get("e")
    
    if a and a.strip() == answers_math2[0]:
        count_math2 += 1
    if b and b.strip() == answers_math2[1]:
        count_math2 += 1
    if c and c.strip() == answers_math2[2]:
        count_math2 += 1
    if d and d.strip() == answers_math2[3]:
        count_math2 += 1
    if e and e.strip() == answers_math2[4]:
        count_math2 += 1
    
    await message.answer(f"У вас {count_math2}/5 <b>правильных</b> ответов.", parse_mode="HTML")
    
    await create_answer(answer_math2=count_math2)
    await state.clear()


# Уровень 3
@router.callback_query(F.data == "three_math")
async def three(callback: CallbackQuery, state: FSMContext):  # исправлено имя one -> three
    await callback.message.answer("Викторина по математике уровень сложный")
    await callback.message.answer("<b>1 вопрос</b> \n 2 в 4 степени", parse_mode="HTML")
    await state.set_state(math3.a)
    await callback.answer()


@router.message(math3.a)
async def a2(message: Message, state: FSMContext):
    await state.set_data({"a2": message.text})
    
    await message.answer("<b>2 вопрос</b> найди дискриминант в уравнении x² - 5x + 4 = 0", parse_mode="HTML")
    await state.set_state(math3.b)


@router.message(math3.b)
async def b2(message: Message, state: FSMContext):
    await state.set_data({"b2": message.text})
    
    await message.answer("<b>3 вопрос</b> Найди корень из 6.25", parse_mode="HTML")
    await state.set_state(math3.c)


@router.message(math3.c)
async def c2(message: Message, state: FSMContext):
    await state.set_data({"c2": message.text})
    
    await message.answer("<b>4 вопрос</b> Запишите число которому равняется x - x/10 = 3/2", parse_mode="HTML")
    await state.set_state(math3.d)


@router.message(math3.d)
async def d2(message: Message, state: FSMContext):
    await state.set_data({"d2": message.text})
    
    await message.answer("<b>5 вопрос</b> log(2) = 8")
    await state.set_state(math3.e)


@router.message(math3.e)
async def e2(message: Message, state: FSMContext):
    await state.set_data({"e2": message.text})
    
    count_math3 = 0
    data = await state.get_data()
    
    a = data.get("a")
    b = data.get("b")
    c = data.get("c")
    d = data.get("d")
    e = data.get("e")
    
    if a and a.strip() == answers_math3[0]:
        count_math3 += 1
    if b and b.strip() == answers_math3[1]:
        count_math3 += 1
    if c and c.strip() == answers_math3[2]:
        count_math3 += 1
    if d and d.strip() == answers_math3[3]:
        count_math3 += 1
    if e and e.strip() == answers_math3[4]:
        count_math3 += 1
    
    await message.answer(f"У вас {count_math3}/5 <b>правильных</b> ответов.", parse_mode="HTML")
    
    await create_answer(answer_math3=count_math3)
    await state.clear()