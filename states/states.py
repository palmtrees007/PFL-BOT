from aiogram.fsm.state import State, StatesGroup


class FSMRegForm(StatesGroup):
    email = State()
    nickname = State()
    password = State()
    repeat_password = State()
    verif_code = State()


class FSMLogFrom(StatesGroup):
    email = State()
    verif_code = State()
    password = State()