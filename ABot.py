from config import TOKEN
import time
import Parsing
from aiogram import Bot, types, Dispatcher, executor

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(msg: types.Message):
    user_id = msg.from_user.id
    user_name = msg.from_user.first_name
    user_full_name = msg.from_user.full_name
    print(user_id, user_full_name, time.asctime())
    await bot.send_message(msg.from_user.id, 'Привет, '+str(user_name)+'.\nЯ бот поиска лекарств в сети аптек Фармакопейка.\nВведите название лекарства:')

@dp.message_handler(content_types=['text'])
async def find(msg: types.Message):
    print(msg.text)
    user_id = msg.from_user.id
    user_full_name = msg.from_user.full_name
    print(user_id, user_full_name, time.asctime())
    name, price, have, url = Parsing.parse(msg.text)
    for i in range(len(name)):
        a = name[i], price[i], have[i], url[i]
        await bot.send_message(msg.chat.id, str(a[0]) + '\nЦена: ' + str(a[1]) + '\nВ наличии: ' + str(a[2]) + '\n' + str(a[3]))
        time.sleep(0.5)