import TBot #telebot
import ABot #aiogram

if __name__ =='__main__':
    ABot.executor.start_polling(ABot.dp)
    # TBot.bot.polling(none_stop=True, interval=0)