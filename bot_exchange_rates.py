from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import json

TOKEN = ""

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

with open('dict_exchanges.json', 'r') as fh:
    dict_exchanges = json.load(fh)

names_buttons = [name for name in dict_exchanges]

dict_exchanges_lower = {}
for key in dict_exchanges:
    dict_exchanges_lower[key.lower()] = dict_exchanges[key]

list_names_cryptos_lower = [key for key in dict_exchanges_lower]
print(list_names_cryptos_lower)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=3)
    keyboard.add(*names_buttons)
    
    await message.reply('Приветсвтую, введите валюту для отображения стоимости:', reply_markup=keyboard)

def message_crypto(dict_exchange):
    return f"""Название:                 {dict_exchange['name']}({dict_exchange['name_crypto']})
Стоимость:              {dict_exchange['price']}
Капитализация:      {dict_exchange['capitalization']}
Объём(24ч.):            {dict_exchange['volume']}
Изменение(24 ч.):  {dict_exchange['change']}"""

@dp.message_handler()
async def crypto(message: types.Message):
    if message.text.lower() in list_names_cryptos_lower:
        dict_exchange = dict_exchanges_lower[message.text.lower()]
        await message.answer(message_crypto(dict_exchange))


if __name__ == '__main__':
    executor.start_polling(dp)
