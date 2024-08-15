from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


#Кнопки авторизации/регистрации
login_inline_btn = InlineKeyboardButton(text='Вход', callback_data='log_callback')
reg_inline_btn = InlineKeyboardButton(text='Регистрация', callback_data='reg_callback')
repeat_code_btn = InlineKeyboardButton(text='Выслать код повторно', callback_data='repeat_code_pressed')
begin_btn = InlineKeyboardButton(text='Начать', callback_data='begin_btn_pressed')
#Кнопки основного меню
profile_btn = InlineKeyboardButton(text='Профиль', callback_data='profile_btn_pressed')
timmates_btn = InlineKeyboardButton(text='Поиск тимметов', callback_data='timmates_btn_pressed')
find_match_btn = InlineKeyboardButton(text='Играть', callback_data='find_match_btn_pressed')
clans_btn = InlineKeyboardButton(text='Кланы', callback_data='clans_btn_pressed')
tournaments_btn = InlineKeyboardButton(text='Турниры', callback_data='tournamets_btn_pressed')
shop_btn = InlineKeyboardButton(text='Магазин', callback_data='shop_btn_pressed')
workout_btn = InlineKeyboardButton(text='Тренировки', callback_data='workout_btn_pressed')
rating_btn = InlineKeyboardButton(text='Рейтинг', callback_data='rating_btn_pressed')


def build_keyboard(*btns, width=1):
    builder = InlineKeyboardBuilder()
    builder.row(*btns, width=width)
    return builder.as_markup()
