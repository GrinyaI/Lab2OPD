import time
import Parsing
import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=["start"])
def start(m, res=False):
    user_id = m.from_user.id
    user_full_name = m.from_user.full_name
    print(user_id, user_full_name, time.asctime())
    bot.send_message(m.chat.id, 'Привет, я бот поиска лекарств в сети аптек Фармакопейка.\nВведите название лекарства:')
@bot.message_handler(content_types=["text"])
def handle_text(message):
    print(message.text)
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    print(user_id, user_full_name, time.asctime())
    name,price,have,url = Parsing.parse(message.text)
    for i in range(len(name)):
        a = name[i], price[i], have[i], url[i]
        bot.send_message(message.chat.id, str(a[0])+'\nЦена: '+str(a[1])+'\nВ наличии: '+str(a[2])+'\n'+str(a[3]))
        time.sleep(0.5)