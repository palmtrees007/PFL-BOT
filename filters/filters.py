from aiogram.filters import BaseFilter
from aiogram.types import Message


class IsValidPasswordFilter(BaseFilter):
    def __init__(self, password):
        self.password = password

    async def __call__(self, message: Message):
        text = message.text
        if len(text) < 8:
            return {'warning': 'len'}
        elif not any(map(lambda x: x.isupper(), text)):
            return {'warning': 'up'}
        elif not any(map(lambda x: x.isdigit(), text)):
            return {'warning': 'no_nums'}
        elif not all(map(lambda x: x.isalpha() and (ord(x) in range(ord('a'), ord('z')+1) or ord(x) in range(ord('A'), ord('Z')+1)), filter(lambda x: x.isalpha(), text))):
            return {'warning': 'no_english'}
        else:
            return {'warning': None}
        