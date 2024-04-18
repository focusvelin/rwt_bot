from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

menu = [
    [InlineKeyboardButton(text="Мои таски", callback_data="list_tasks"),
    InlineKeyboardButton(text="Добавить таску", callback_data="add_task"),
    InlineKeyboardButton(text="Запланировать таску", callback_data="plan_task")],
    [InlineKeyboardButton(text="Test", callback_data="test")]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)

valid_task = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Да", callback_data="task_valid"),
    InlineKeyboardButton(text="Нет", callback_data="task_not_valid")]
])

back_button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Назад в меню", callback_data="back_to_menu")]])