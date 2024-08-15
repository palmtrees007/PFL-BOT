from aiogram import Router, F
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import ReplyKeyboardRemove

from lexicon.lexicon import LEXICON, reply_btn_lex
from keyboards.reply_keyboards import main_menu_keyboard
from states.states import FSMMenu


main_router = Router()


@main_router.callback_query(F.data == 'begin_btn_pressed')
async def process_begin_btn_pressed(callback: CallbackQuery, state: FSMContext):
    await state.set_state(FSMMenu.in_menu)
    await callback.message.delete()
    await callback.message.answer(text=LEXICON['main_menu'],
                                  reply_markup=main_menu_keyboard)
    

@main_router.message(F.text == reply_btn_lex['play'], StateFilter(FSMMenu.in_menu))
async def process_play_pressed(message: Message, state: FSMContext):
    await message.answer(text=LEXICON['find_game'], reply_markup=ReplyKeyboardRemove())

    #Игрок подключается к лобби и идет ожидание други игроков

    await state.set_state(FSMMenu.search_game)
    await message.answer(text=LEXICON['in_lobby'])


@main_router.message(F.text == reply_btn_lex['search_teammates'], StateFilter(FSMMenu.in_menu))
async def process_search_team_pressed(message: Message, state: FSMContext):
    pass


@main_router.message(F.text == reply_btn_lex['tournamets'], StateFilter(FSMMenu.in_menu))
async def process_tournamets_pressed(message: Message, state: FSMContext):
    pass


@main_router.message(F.text == reply_btn_lex['clans'], StateFilter(FSMMenu.in_menu))
async def process_clans_pressed(message: Message, state: FSMContext):
    pass


@main_router.message(F.text == reply_btn_lex['shop'], StateFilter(FSMMenu.in_menu))
async def process_shop_pressed(message: Message, state: FSMContext):
    pass


@main_router.message(F.text == reply_btn_lex['rating'], StateFilter(FSMMenu.in_menu))
async def process_rating_pressed(message: Message, state: FSMContext):
    pass


@main_router.message(F.text == reply_btn_lex['profile'], StateFilter(FSMMenu.in_menu))
async def process_profile_pressed(message: Message, state: FSMContext):
    state.set_state(FSMMenu.in_profile)
    


@main_router.message(F.text == reply_btn_lex['workout'], StateFilter(FSMMenu.in_menu))
async def process_orkout_pressed(message: Message, state: FSMContext):
    pass


