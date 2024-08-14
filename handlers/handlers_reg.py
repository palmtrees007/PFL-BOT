#Это файл с хендлерами, срабатывающими в состоянии регистрации в аккаунт пользователя

from aiogram import Router, F
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state

from lexicon.lexicon import LEXICON
from keyboards.inline_keyboards import build_keyboard, login_inline_btn, reg_inline_btn, repeat_code_btn
from filters.filters import IsValidPasswordFilter
from states.states import FSMRegForm, FSMLogFrom
from utils.utils import check_email

from random import randint



reg_router = Router()


@reg_router.message(CommandStart(), StateFilter(default_state))
async def process_start_command(message: Message) -> None:
    await message.answer(text=LEXICON['greeting'],
                         reply_markup=build_keyboard(login_inline_btn, reg_inline_btn))
    


@reg_router.callback_query(F.data == 'reg_callback')
async def process_reg_btn_pressed(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.message.delete()
    await callback.message.answer(text=LEXICON['requests_email'])
    await callback.message.answer(text='Чтобы отменить регистрацию введите /cancel')
    await state.set_state(FSMRegForm.email)


@reg_router.message(Command(commands='cancel'), StateFilter(FSMRegForm.nickname,  FSMRegForm.password, FSMRegForm.email, FSMRegForm.verif_code,
                                                            FSMLogFrom.password, FSMLogFrom.email, FSMRegForm.repeat_password,
                                                            FSMLogFrom.verif_code ))
async def process_cancel_command(message: Message, state: FSMContext):
    await state.clear()
    await process_start_command(message)


@reg_router.message(FSMRegForm.email)
async def process_nickname_sent(message: Message, state: FSMContext) -> None:
    if check_email(message.text):
        await state.update_data(email=message.text)
        
        await state.set_state(FSMRegForm.verif_code)
        await state.update_data(verif_code='1000')
        #Здесь на почту присылается случайный код подтверждения
        
        await message.answer(text=LEXICON['confirmation_code_sent'], reply_markup=build_keyboard(repeat_code_btn))

    
@reg_router.callback_query(F.data == 'repeat_code_pressed', StateFilter(FSMRegForm.verif_code))
async def process_repeat_code_btn_pressed(callback: CallbackQuery, state: FSMContext):
    await callback.answer(text='Код выслан повторно')
    
    await state.update_data(verif_code='1100')
    #Снова высылается новый код подтверждения


@reg_router.message(StateFilter(FSMRegForm.verif_code))
async def process_code_sent(message: Message, state: FSMContext):
    code = message.text
    true_code = await state.get_data()
    if code != true_code['verif_code']:
        await message.answer(text=LEXICON['false_code'], reply_markup=build_keyboard(repeat_code_btn))
    else:
        await message.answer(text=LEXICON['email_confirmed'])
        await message.answer(text=LEXICON['requests_nick'])
        await state.set_state(FSMRegForm.nickname)


@reg_router.message(StateFilter(FSMRegForm.nickname))
async def process_nick_sent(message: Message, state: FSMContext):
    await state.update_data(nickname=message.text)
    await message.answer(text=LEXICON['requests_new_password'])
    await state.set_state(FSMRegForm.password)


@reg_router.message(IsValidPasswordFilter(F.text), StateFilter(FSMRegForm.password))
async def process_password_sent(message: Message, state: FSMContext, warning: str | None) -> None:
    if warning == 'len':
        await message.answer(text=LEXICON['not_enough_len'])
    elif warning == 'up':
        await message.answer(text=LEXICON['not_enough_up'])
    elif warning == 'special':
        await message.answer(text=LEXICON['not_special'])
    elif warning == 'no_nums':
        await message.answer(text=LEXICON['no_nums'])
    elif warning == 'no_english':
        await message.answer(text=LEXICON['no_english'])
    else:
        await message.answer(text=LEXICON['valid_password'])
        await state.update_data(password=message.text)
        await state.set_state(FSMRegForm.repeat_password)


@reg_router.message(StateFilter(FSMRegForm.repeat_password))
async def process_repeat_password_sent(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    if message.text == data['password']:
        await message.answer(text=LEXICON['password_confirmed'])

        #Тут надо добавить запись полученных значений в бд


        await state.clear()

    else:
        await message.answer(text=LEXICON['password_not_confired'])
        await process_password_sent(message, state)

