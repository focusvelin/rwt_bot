from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def hour_buttons():
    builder = InlineKeyboardBuilder()
    for hour in range(0, 10):
        builder.button(text=f'0{hour}', callback_data=f'hour_0{hour}')
    for hour in range(10, 24):
        builder.button(text=hour, callback_data=f'hour_{hour}')   
    return builder.adjust(4, 4).as_markup()

def minute_buttons():
    builder = InlineKeyboardBuilder()
    for minute in range(0, 10):
        builder.button(text=f'0{minute}', callback_data=f'minute_0{minute}')
    for minute in range(10, 60):
        builder.button(text=minute, callback_data=f'minute_{minute}')   
    return builder.adjust(8, 8).as_markup()
