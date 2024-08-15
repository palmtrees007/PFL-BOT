from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon import reply_btn_lex


profile_btn = KeyboardButton(text=reply_btn_lex['profile'])
teammates_btn = KeyboardButton(text=reply_btn_lex['search_teammates'])
find_match_btn = KeyboardButton(text=reply_btn_lex['play'])
clans_btn = KeyboardButton(text=reply_btn_lex['clans'])
tournaments_btn = KeyboardButton(text=reply_btn_lex['tournamets'])
shop_btn = KeyboardButton(text=reply_btn_lex['shop'])
workout_btn = KeyboardButton(text=reply_btn_lex['workout'])
rating_btn = KeyboardButton(text=reply_btn_lex['rating'])


def build_reply_keyboard(*btns, width=1):
    builder = ReplyKeyboardBuilder()
    builder.row(*btns, width=width)
    return builder.as_markup()

main_menu_keyboard = build_reply_keyboard(find_match_btn, teammates_btn, tournaments_btn, 
                                          clans_btn, shop_btn, rating_btn, profile_btn, workout_btn, width=2)