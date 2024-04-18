from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import or_f
from aiogram.fsm.context import FSMContext
from aiogram.types.callback_query import CallbackQuery
from states import Task
from database.requests import get_user, create_user, create_task
from utils.time import str_to_timestamp

import keyboards.kb as kb
import keyboards.time_kb as t_kb

router = Router()

@router.callback_query(F.data == "add_task")
async def add_task(clbk: CallbackQuery, state: FSMContext):
    await clbk.message.edit_text("Введите краткое описание таски", reply_markup=kb.back_button)
    await state.set_state(Task.set_descr)
    
@router.message(Task.set_descr)
async def task_descr(msg: Message, state: FSMContext):
    await state.update_data(descr=msg.text)
    await msg.answer("Выберите время начала таски: часы", reply_markup=t_kb.hour_buttons())
    await state.set_state(Task.set_begin_time)

@router.callback_query(Task.set_begin_time)
async def task_begin(clbk: CallbackQuery, state: FSMContext):
    if clbk.data.startswith('hour_'):
        await state.update_data(begin_hour=clbk.data.split('_')[1])
        await clbk.message.edit_text("Выберите время начала таски: минуты", reply_markup=t_kb.minute_buttons())
    if clbk.data.startswith('minute_'): 
        await state.update_data(begin_minute=clbk.data.split('_')[1])  
        await clbk.message.edit_text("Выберите время окончания таски: часы", reply_markup=t_kb.hour_buttons())
        await state.set_state(Task.set_end_time)

@router.callback_query(Task.set_end_time)
async def task_end(clbk: CallbackQuery, state: FSMContext):
    if clbk.data.startswith('hour_'):
        await state.update_data(end_hour=clbk.data.split('_')[1])
        await clbk.message.edit_text("Выберите время окончания таски: минуты", reply_markup=t_kb.minute_buttons())
    if clbk.data.startswith('minute_'): 
        await state.update_data(end_minute=clbk.data.split('_')[1])  
        data = await state.get_data()
        task_str = f"{data['begin_hour']}:{data['begin_minute']}-{data['end_hour']}:{data['end_minute']} {data['descr']}"
        await clbk.message.edit_text(f"{task_str}\n\nВерны ли введеные данные?", reply_markup=kb.valid_task)
        await state.set_state(Task.check_info)
    
 
@router.callback_query(Task.check_info, F.data.in_(['task_valid', 'task_not_valid']))
async def task_validate(callback: CallbackQuery, state: FSMContext):

    if callback.data == 'task_valid':
        await state.update_data(user_id=callback.message.chat.id)
        task_data = await state.get_data()
        if await get_user(task_data["user_id"]) is None:
            await create_user(task_data["user_id"], callback.message.chat.username)

        begin_time = str_to_timestamp(task_data['begin_hour'], task_data['begin_minute'])
        end_time = str_to_timestamp(task_data['end_hour'], task_data['end_minute'])
        await create_task(task_data["descr"], begin_time, end_time, task_data["user_id"])
        await callback.message.edit_text("Таска добавлена", reply_markup=kb.back_button) 
    else:
        await callback.message.edit_text("Таска не добавлена", reply_markup=kb.back_button)       
    await state.clear()

