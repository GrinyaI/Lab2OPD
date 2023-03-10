import time
import Parsing
import telebot

with open('Token','r') as tok:
    bot = telebot.TeleBot(tok.read())
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Привет, я бот поиска лекарств в сети аптек Фармакопейка.\nВведите название лекарства:')
@bot.message_handler(commands=["0110"])
def stop(m, res=False):
    bot.stop_polling()
@bot.message_handler(content_types=["text"])
def handle_text(message):
    print(message.text)
    name,price,have,url = Parsing.parse(message.text)
    for i in range(len(name)):
        a = name[i], price[i], have[i], url[i]
        bot.send_message(message.chat.id, str(a[0])+'\nЦена: '+str(a[1])+'\nВ наличии: '+str(a[2])+'\n'+str(a[3]))
        time.sleep(0.5)