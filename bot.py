import telebot
token='5466316605:AAHccYQhfU4pPnw1s9FqyCDx1a-A-yCTTFQ'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет ✌️ ")
bot.polling(none_stop=True)