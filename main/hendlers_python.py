from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from .keyboard import python
from aiogram.fsm.context import FSMContext
from state.state import python1, python2, python3
from database import create_answer

router = Router()
one_python_answer = ["1", "3", "3", "2", "1"]
two_python_answer = ["1", "2", "3", "3", "1"]
three_python_answer = ["3", "2", "2", "1", "1"]

@router.message(Command("python"))
async def python(message:Message):
    await message.answer("Выберите уровень сложности", reply_markup=python)

#уровень 1
@router.callback_query(F.data=="one_python")
async def one_python(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Python уровень Легкий \n\n В ответ писать только цифры правильного ответа")
    await callback.message.answer("1 вопрос \n\n Какая функция выводит текст в консоль \n 1.) print()\n 2.) input() \n 3.) log()")
    await state.set_state(python1.a3)
    await callback.answer()

@router.message(python1.a)
async def a3(message:Message, state: FSMContext):
    await message.answer("2 вопрос \n\n Какая функция запрашивает данные \n 1.) print()\n 2.) request()\n3.) input()")
    await state.set_state(python1.b)

@router.message(python1.b)
async def b3(message:Message, state: FSMContext):
    await message.answer("3 вопрос \n\n Какая функция может выводить что то бесконечное количество \n 1.)for \n 2.)infinity \n3.) while")
    await state.set_state(python1.c)

@router.message(python1.c)
async def c3(message:Message, state: FSMContext):
    await message.answer("4 вопрос \n\n Какая функция может что-то выводить определеное количество раз \n 1.) while\n 2.) for\n3.) infinity")
    await state.set_state(python1.d)

@router.message(python1.d)
async def d3(message:Message, state: FSMContext):
    await message.answer("5 вопрос \n\n  Какая функция рандомно что-то генерирует\n 1.) randing\n 2.) random\n3.) rand ")
    await state.set_state(python1.e)
    count_python1 = 0
    data3 = await state.get_data()
    
    a=data3.get("a")
    b=data3.get("b")
    c=data3.get("c")
    d=data3.get("d")
    e=data3.get("e")

    if a == one_python_answer[0]:
        count_python1 += 1
    if b == one_python_answer[1]:
        count_python1 += 1
    if c == one_python_answer[2]:
        count_python1 += 1
    if d == one_python_answer[3]:
        count_python1 += 1
    if e == one_python_answer[4]:
        count_python1 += 1
    await message.answer(f"У вас {count_python1}/5 <b>правильных</b> ответов.",
               parse_mode="HTML")

    await create_answer(
        answer_python1 = count_python1
    )
    await state.clear()


#уровень 2

@router.callback_query(F.data=="two_python")
async def two_python(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Python уровень Средний \n\n В ответ писать только цифры правильного ответа")
    await callback.message.answer("1 вопрос \n\n Какая функция дабовляет что-то в конец списка \n 1.) .append\n 2.) .pop\n 3.) .ending")
    await state.set_state(python2.a4)
    await callback.answer()

@router.message(python2.a)
async def a4(message:Message, state: FSMContext):
    await message.answer("2 вопрос \n\n Какая функция делает так чтобы в for что то выводилось несколько раз\n 1.) several\n 2.) range\n3.) once")
    await state.set_state(python2.b)

@router.message(python2.b)
async def b4(message:Message, state: FSMContext):
    await message.answer("3 вопрос \n\n Как сделать так чтобы цикл while был бесконечным \n 1.)while False \n 2.)while infinite\n3.) while True")
    await state.set_state(python2.c)

@router.message(python2.c)
async def c4(message:Message, state: FSMContext):
    await message.answer("4 вопрос \n\n Чем отличается кортеж от списка \n 1.) В нем () скобки\n 2.) В нем {} скобки\n3.) Он не изменяется")
    await state.set_state(python2.d)

@router.message(python2.d)
async def d4(message:Message, state: FSMContext):
    await message.answer("5 вопрос \n\n Какая функция что то рандомно выбирает \n 1.) randint\n 2.) random\n3.) rand")
    await state.set_state(python2.e)
    count_python2 = 0
    data3 = await state.get_data()
    
    a=data3.get("a") 
    b=data3.get("b") 
    c=data3.get("c")
    d=data3.get("d")
    e=data3.get("e")

    if a == two_python_answer[0]:
        count_python2 += 1
    if b == two_python_answer[1]:
        count_python2 += 1
    if c == two_python_answer[2]:
        count_python2 += 1
    if d == two_python_answer[3]:
        count_python2 += 1
    if e == two_python_answer[4]:
        count_python2 += 1
    await message.answer(f"У вас {count_python2}/5 <b>правильных</b> ответов.",
               parse_mode="HTML")

    await create_answer(
        answer_python2 = count_python2
    )
    await state.clear()

#уровень 3

@router.callback_query(F.data=="three_python")
async def three_python(callback: CallbackQuery,  state: FSMContext):
    await callback.message.answer("Python уровень Сложный \n\n В ответ писать только цифры правильного ответа")
    await callback.message.answer("1 вопрос \n\n Как создать функцию \n 1.) funcio \n 2.) funkcion \n 3.) def")
    await state.set_state(python3.a5)
    await callback.answer()

@router.message(python3.a)
async def a5(message:Message, state: FSMContext):
    await message.answer("2 вопрос \n\n Как в списке отсортировать элементы \n 1.) sert\n 2.) sort\n3.) sorting")
    await state.set_state(python3.b)


@router.message(python3.b)
async def b5(message:Message, state: FSMContext):
    await message.answer("3 вопрос \n\n Как объявить класс \n 1.)objekt \n 2.)class \n3.) close")
    await state.set_state(python3.c)


@router.message(python3.c)
async def c5(message:Message, state: FSMContext):
    await message.answer("4 вопрос \n\n Как вытощить что-то из списка \n 1.) По индексу\n 2.) По ключу\n3.) По значению")
    await state.set_state(python3.d)

@router.message(python3.d)
async def d5(message:Message, state: FSMContext):
    await message.answer("5 вопрос \n\n Какой командой что-то установить \n 1.) pip \n2.)establish \n3.) installation")
    await state.set_state(python3.e)
    count_python3 = 0
    data5 = await state.get_data()
    
    a=data5.get("a") 
    b=data5.get("b") 
    c=data5.get("c")
    d=data5.get("d")
    e=data5.get("e")

    if a == three_python_answer[0]:
        count_python3 += 1
    if b == three_python_answer[1]:
        count_python3 += 1
    if c == three_python_answer[2]:
        count_python3 += 1
    if d == three_python_answer[3]:
        count_python3 += 1
    if e == three_python_answer[4]:
        count_python3 += 1
    await message.answer(f"У вас {count_python3}/5 <b>правильных</b> ответов.",
               parse_mode="HTML")


    await create_answer(
        answer_python3 = count_python3
    )
    await state.clear()