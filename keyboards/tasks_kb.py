from aiogram.utils.keyboard import InlineKeyboardBuilder

def task_list_buttons(tasks_list):
    builder = InlineKeyboardBuilder()

    for task in tasks_list:
        begin_time = task.begin_time.strftime("%H:%M")
        end_time = task.end_time.strftime("%H:%M")
        builder.button(text=f'{begin_time}-{end_time} {task.descr}', callback_data=task.id)
    builder.button(text="Назад", callback_data="back_to_date")
    return builder.adjust(1).as_markup()

def task_date_buttons(task_dates):
    builder = InlineKeyboardBuilder()

    for date in task_dates:
        builder.button(text=date, callback_data=date)
    builder.button(text="Назад", callback_data="back_to_menu")
    return builder.adjust(1).as_markup()
    
