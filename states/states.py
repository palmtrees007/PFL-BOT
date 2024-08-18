from aiogram.fsm.state import State, StatesGroup


class FSMRegForm(StatesGroup):
    email = State()
    nickname = State()
    password = State()
    repeat_password = State()
    verif_code = State()
    verif_code_tr = State()
    between = State()
    tries = State()


class FSMLogForm(StatesGroup):
    email = State()
    verif_code = State()
    password = State()
    tries = State()
    between = State()


class FSMMenu(StatesGroup):
    in_menu = State()
    search_game = State()
    in_profile = State()