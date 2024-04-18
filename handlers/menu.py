from aiogram import  Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.types.callback_query import CallbackQuery
from aiogram.fsm.context import FSMContext
from states import Menu

import keyboards.kb as kb
import text

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message, state: FSMContext):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)

@router.message(Menu.in_menu)
async def show_menu(msg: Message):
    await msg.edit_text("Главное меню", reply_markup=kb.menu)

@router.callback_query(F.data == "back_to_menu")
async def back_to_menu(clbk: CallbackQuery, state: FSMContext):
    await state.set_state(Menu.in_menu)
    await show_menu(clbk.message)