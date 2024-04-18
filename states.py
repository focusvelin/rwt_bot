from aiogram.fsm.state import StatesGroup, State

class Task(StatesGroup):
    set_descr = State()
    set_begin_time = State()
    set_end_time = State()
    check_info = State()
    select_task = State()

class Menu(StatesGroup):
    in_menu = State()