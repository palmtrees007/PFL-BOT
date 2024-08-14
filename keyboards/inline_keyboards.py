from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


login_inline_btn = InlineKeyboardButton(text='Вход', callback_data='log_callback')
reg_inline_btn = InlineKeyboardButton(text='Регистрация', callback_data='reg_callback')
repeat_code_btn = InlineKeyboardButton(text='Выслать код повторно', callback_data='repeat_code_pressed')


def build_keyboard(*btns, width=1):
    builder = InlineKeyboardBuilder()
    builder.row(*btns, width=width)
    return builder.as_markup()