from aiogram import F, Router
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup, default_state
import aiomysql
from random import randint

from lexicon.lexicon import LEXICON
from states.states import FSMLogForm
from utils.utils import check_email, send_email
from db.db_comm import check, check_password
from keyboards.inline_keyboards import begin_btn, build_keyboard

log_router = Router()


@log_router.callback_query(F.data == 'log_callback')
async def process_log_btn_pressed(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await callback.message.answer(text=LEXICON['requests_email'])
    await callback.message.answer(text='Чтобы отменить вход в аккаунт введите /cancel')
    await state.set_state(FSMLogForm.email)


@log_router.message(StateFilter(FSMLogForm.email))
async def process_email_log_sent(message: Message, state: FSMContext, pool: aiomysql.Pool):
    if await check_email(message.text):
        ch = await check(message.text, pool)
        if not ch:
            if len(message.text) <= 50:
                await state.update_data(email=message.text)
                await state.set_state(FSMLogForm.verif_code)
                code = randint(100000, 999999)
                await state.update_data(verif_code=code, tries=3)
                await message.answer(text=LEXICON['confirmation_code_sent'])
                await send_email(message.text, code)
            else:
                await message.answer(text='Слишком длинная почта')
        else:
            await message.answer(text='Уже есть аккаунт, зарегистрированный на эту почту')
    else:
        await message.answer(text='Неверная почта')

    
@log_router.message(StateFilter(FSMLogForm.verif_code))
async def process_verif_code_sent_log(message: Message, state: FSMContext):
    code = message.text
    data = await state.get_data()
    if code != str(data['verif_code']):
        await state.update_data(tries=data['tries']-1)
        await message.answer(text=f'Неверный код. Осталось попыток: {data["tries"]}')
    else:
        await message.answer(text=LEXICON['email_confirmed'])
        await message.answer(text=LEXICON['requests_log_pas'])
        await state.update_data(tries=3)
        await state.set_state(FSMLogForm.password)


@log_router.message(StateFilter(FSMLogForm.password))
async def process_password_log_sent(message: Message, state: FSMContext, pool: aiomysql.Pool):
    data = await state.get_data()
    if data['tries'] > 0:
        if await check_password(message.text, data['email'], pool):
            await message.answer(text=LEXICON['psw_confirmed_log'], reply_markup=build_keyboard(begin_btn))
            await state.set_state(FSMLogForm.between)
        else:
            await state.update_data(tries=data['tries']-1)
            await message.answer(text=f'Неверный пароль. Осталось попыток: {data["tries"]}')
    else:
        await message.answer(text='Попытки кончились. Чтобы пройти вход в аккаунт повторно, введите /cancel')