import os
import types
import telebot
from telebot import types
from buttonmenu import *
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

bot = telebot.TeleBot(API_KEY)

#markup = types.ReplyKeyboardMarkup(row_width=2)
#itembtn1 = types.KeyboardButton('a')
#itembtn2 = types.KeyboardButton('v')
#itembtn3 = types.KeyboardButton('d')
#markup.add(itembtn1, itembtn2, itembtn3)


#Greeting Message

@bot.message_handler(commands=['start'])
def greet(message):
    markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    trackbtn = types.KeyboardButton('➕ Track',)
    listbtn = types.KeyboardButton('📃 List')
    helpbtn = types.KeyboardButton('❓ Help')
    sharebtn = types.KeyboardButton('📤 Share')
    modifybtn = types.KeyboardButton('✏️ Modify')
    removebtn = types.KeyboardButton('🗑️ Remove')
    
    markup.add(trackbtn, listbtn, helpbtn, sharebtn, modifybtn,removebtn)
    bot.send_message(message.chat.id, "👋 Hi " + message.from_user.first_name + ", my name is UTrackBot and I can help you keep track of your shipments.")
    bot.send_message(message.chat.id, "✅ What you need to know:\n\n1️⃣ This service is free and unlimited.\n\n2️⃣ To add a new shipment, tap ➕ *Track* down here, or send the tracking number directly.\n\n3️⃣ For help if you face a problem, tap ❓ *Help*.", parse_mode='Markdown', reply_markup=markup)
    #bot.send_message(message.from_user.id, "*hello*", parse_mode='Markdown')    
    

#Tracking

@bot.message_handler(content_types=['text'])
def button_menu(message):
    text = message.text.lower()

    #track_option
    if 'track' in text:
        track_id = bot.send_message(message.chat.id, "📦 I'm ready. Enter your tracking number :\n\n/cancel".format(message.from_user, bot.get_me()))
        bot.register_next_step_handler(track_id, trackid_handler)
        

    #list_option
    elif 'list' in text:
        list_shipment(message)

    #remove_option
    elif 'remove' in text:
        remove_shipment(message)

    #share_option
    elif 'share' in text:
        share_shipment(message)
    
    #modify_option
    elif 'modify' in text:
        modify_shipment(message)
    
    #help_option
    elif 'help' in text:
        help(message)
    
    #cancel_command
    #elif 'cancel' in text:
    #    cancel(message)
    
    else:
        bot.send_message(message.chat.id, "❗ I don't understand. Please try again!")

#Tracking_number_exception
def trackid_handler(message):
    track_id = message.text
    if 'cancel' in track_id:
        cancel(message)
    elif len(track_id) > 30:
        bot.send_message(message.chat.id, "Tracking number cannot be longer than 30 characters. Try again!") 





'''
@bot.message_handler(content_types=["text"])
def add(message):
  sent_mg = bot.send_message(message.chat.id, "Enter first number")
  bot.register_next_step_handler(sent_sg, name_handler)
  sent_msg = bot.send_message(message.chat.id, "Enter second number")

def name_handler(message):
    num1 = message.text
    bot.send_message(message.chat.id, f"Your name is {num1}")
    bot.send_message(message.chat.id, "Sum is " + str(sum))
'''


bot.polling()