from aiogram import F, Router
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup, default_state

from lexicon.lexicon import LEXICON
from states.states import FSMLogFrom


log_router = Router()


@log_router.callback_query(F.data == 'log_callback')
async def process_log_btn_pressed(callback: CallbackQuery, state: FSMContext):
    pass


@log_router.message(StateFilter(FSMLogFrom.password))
async def process_password_sent(message: Message, state: FSMContext):
    pass