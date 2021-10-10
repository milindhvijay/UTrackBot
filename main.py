import os
import telebot
from telebot.types import Update

API_KEY = '2074114916:AAGIMQ3J4whzLqmMMiTJqLtSNrgwrQdZ9_w'
bot = telebot.TeleBot(API_KEY)

#print(emoji.demojize("👋"))

@bot.message_handler(commands=["start","hello"])
def greet(message):
    bot.send_message(message.chat.id, "👋 Hi, my name is UTrackBot and I can help you keep track of your shipments")
    bot.send_message(message.chat.id, "✅ What you need to know:\n\n1️⃣ This service is free and unlimited.\n\n2️⃣ To add a new shipment, tap ➕ *Track* down here, or send the tracking number directly.\n\n3️⃣ For help if you face a problem, tap ❓ *Help*.", parse_mode='Markdown')
    bot.send_message(message.from_user.id, "*hello*", parse_mode='Markdown')    
    

@bot.message_handler(commands=['track', 'Track'])
def track(message):
    bot.send_message(message.chat.id, "📦 I'm ready. Enter your tracking number :")

@bot.message_handler(commands=['help', 'Help'])
def help(message):
    bot.send_message(message.chat.id, "💬 Commands :")

bot.polling()