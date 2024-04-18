from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import or_f
from aiogram.fsm.context import FSMContext
from aiogram.types.callback_query import CallbackQuery
from states import Task
from database.requests import get_task_list, get_user, get_task_dates
from datetime import timedelta
import keyboards.tasks_kb as kb

router = Router()

@router.callback_query(or_f(F.data == "list_tasks", F.data == 'back_to_date'))
async def select_date(clbk: CallbackQuery, state: FSMContext):
    task_dates = await get_task_dates(clbk.message.chat.id)
    await clbk.message.edit_text(text="Выберите дату", reply_markup=kb.task_date_buttons(task_dates))
    await state.set_state(Task.select_task)

@router.callback_query(Task.select_task)
async def select_task(clbk: CallbackQuery, state: FSMContext):
    user_id = clbk.message.chat.id
    date = clbk.data
    task_list = await get_task_list(user_id, date)
    await clbk.message.edit_text(text="Выберите таску", reply_markup=kb.task_list_buttons(task_list))
    await state.clear()


    


    
    
    