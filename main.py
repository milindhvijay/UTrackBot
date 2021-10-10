import os
import types
import telebot
from telebot.types import Update

API_KEY = '2074114916:AAGIMQ3J4whzLqmMMiTJqLtSNrgwrQdZ9_w'
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=["start","hello"])
def greet(message):
    bot.send_message(message.chat.id, "👋 Hi " + message.from_user.first_name + ", my name is UTrackBot and I can help you keep track of your shipments")
    bot.send_message(message.chat.id, "✅ What you need to know:\n\n1️⃣ This service is free and unlimited.\n\n2️⃣ To add a new shipment, tap ➕ *Track* down here, or send the tracking number directly.\n\n3️⃣ For help if you face a problem, tap ❓ *Help*.", parse_mode='Markdown')
    #bot.send_message(message.from_user.id, "*hello*", parse_mode='Markdown')    
    

@bot.message_handler(commands=['track', 'Track'])
def track(message):
    track_id = bot.send_message(message.chat.id, "📦 I'm ready. Enter your tracking number :".format(message.from_user, bot.get_me()))
    bot.register_next_step_handler(track_id, trackid_handler)

def trackid_handler(message):
    track_id = message.text
    if len(track_id) > 30:
        bot.send_message(message.chat.id, "Tracking number cannot be longer than 30 characters. Try again!") 



@bot.message_handler(commands=['help', 'Help'])
def help(message):
    bot.send_message(message.chat.id, "💬 Commands :")



@bot.message_handler(content_types=["text"])
def add(message):
  sent_mg = bot.send_message(message.chat.id, "Enter first number")
  bot.register_next_step_handler(sent_sg, name_handler)
  sent_msg = bot.send_message(message.chat.id, "Enter second number")

def name_handler(message):
    num1 = message.text
    bot.send_message(message.chat.id, f"Your name is {num1}")
    bot.send_message(message.chat.id, "Sum is " + str(sum))


  
  


bot.polling()