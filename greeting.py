import os
import types
import telebot
from telebot import types
from buttonmenu import *
from dotenv import load_dotenv

load_dotenv()

BOT_API_KEY = os.getenv('BOT_API_KEY')

bot = telebot.TeleBot(BOT_API_KEY)

def greetings():
    @bot.message_handler(commands=['start'])
    def greet(message):
        markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
        trackbtn = types.KeyboardButton('➕ Track',)
        listbtn = types.KeyboardButton('📃 List')
        helpbtn = types.KeyboardButton('❓ Help')
        sharebtn = types.KeyboardButton('📤 Share')
        modifybtn = types.KeyboardButton('✏️ Modify')
        removebtn = types.KeyboardButton('🗑️ Remove')

        markup.add(trackbtn, listbtn, helpbtn, sharebtn, modifybtn, removebtn)
        bot.send_message(message.chat.id, "👋 Hi " + message.from_user.first_name +
                     ", my name is UTrackBot and I can help you keep track of your shipments.")
        bot.send_message(message.chat.id, "✅ What you need to know:\n\n1️⃣ This service is free and unlimited.\n\n2️⃣ To add a new shipment, tap ➕ *Track* down here, or send the tracking number directly.\n\n3️⃣ For help if you face a problem, tap ❓ *Help*.", parse_mode='Markdown', reply_markup=markup)
    #bot.send_message(message.from_user.id, "*hello*", parse_mode='Markdown')