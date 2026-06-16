from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


math = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1 уровень - Легкий", callback_data="one_math")],
        [InlineKeyboardButton(text="2 уровень Средний", callback_data="two_math")],
        [InlineKeyboardButton(text="3 уровень Сложный", callback_data="three_math")]
    ]
)


python = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1 уровень - Легкий", callback_data="one_python")],
        [InlineKeyboardButton(text="2 уровень - Средний", callback_data="two_python")],
        [InlineKeyboardButton(text="3 уровень - Сложный", callback_data="three_python")]
    ]
)


robotics = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1 уровень - Легкий", callback_data="one_robotics")],
        [InlineKeyboardButton(text="2 уровень - Сложный", callback_data="two_robotics")]
    ]
)


quest = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Камень", callback_data="stone"),
            InlineKeyboardButton(text="Ножницы", callback_data="scissors"),
            InlineKeyboardButton(text="Бумага", callback_data="paper")
        ]
    ]
)


choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Согласиться", callback_data="yes")],
        [InlineKeyboardButton(text="Отказаться", callback_data="no")]
    ]
)


a = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="А - хорошая идея", callback_data="player_a1"),
            InlineKeyboardButton(text="Б - мне это не нравится", callback_data="player_b1")
        ]
    ]
)


b = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="А - закричать что нельзя этого делать", callback_data="player_a2"),
            InlineKeyboardButton(text="Б - промолчать", callback_data="player_b2")
        ]
    ]
)