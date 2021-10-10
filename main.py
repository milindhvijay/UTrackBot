import os
import telebot

API_KEY = ''
bot = telebot.TeleBot(API_KEY)

#print(emoji.demojize("👋"))

@bot.message_handler(commands=['start'])
def greet(message):
    bot.send_message(message.chat.id, "👋 Hi, my name is UTrackBot and I can help you keep track of your shipments")
    bot.send_message(message.chat.id, "✅ What you need to know:\n\n1️⃣ This service is free and unlimited.\n\n2️⃣ To add a new shipment, tap ➕ *Track* down here, or send the tracking number directly.\n\n3️⃣ For help if you face a problem, tap ❓ *Help*.", parse_mode='Markdown')
    #bot.send_message(message.chat.id, "*hello*", parse_mode='Markdown')
    


bot.polling()