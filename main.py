import os
import types
import telebot
from telebot import types

API_KEY = '2074114916:AAGIMQ3J4whzLqmMMiTJqLtSNrgwrQdZ9_w'
bot = telebot.TeleBot(API_KEY)

#markup = types.ReplyKeyboardMarkup(row_width=2)
#itembtn1 = types.KeyboardButton('a')
#itembtn2 = types.KeyboardButton('v')
#itembtn3 = types.KeyboardButton('d')
#markup.add(itembtn1, itembtn2, itembtn3)


#Greeting Message

@bot.message_handler(commands=['start'])
def greet(message):
    markup = types.ReplyKeyboardMarkup(row_width=3)
    itembtn1 = types.KeyboardButton('➕ Track',)
    itembtn2 = types.KeyboardButton('📃 List')
    itembtn3 = types.KeyboardButton('❓ Help')
    itembtn4 = types.KeyboardButton('✏️ Modify')
    itembtn5 = types.KeyboardButton('🗑️ Remove')
    itembtn6 = types.KeyboardButton('Unnamed')
    markup.add(itembtn1, itembtn2, itembtn3,itembtn4,itembtn5,itembtn6)
    bot.send_message(message.chat.id, "👋 Hi " + message.from_user.first_name + ", my name is UTrackBot and I can help you keep track of your shipments.")
    bot.send_message(message.chat.id, "✅ What you need to know:\n\n1️⃣ This service is free and unlimited.\n\n2️⃣ To add a new shipment, tap ➕ *Track* down here, or send the tracking number directly.\n\n3️⃣ For help if you face a problem, tap ❓ *Help*.", parse_mode='Markdown', reply_markup=markup)
    #bot.send_message(message.from_user.id, "*hello*", parse_mode='Markdown')    
    

#Tracking

@bot.message_handler(content_types=['text'])
def button_menu(message):
    text = message.text.lower()
    #track_option
    if 'track' in text:
        track_id = bot.send_message(message.chat.id, "📦 I'm ready. Enter your tracking number :".format(message.from_user, bot.get_me()))
        bot.register_next_step_handler(track_id, trackid_handler)

    #list_option
    if 'list' in text:
        bot.send_message(message.chat.id, "You are not tracking any shipments. Start by using the command /track")      

    #remove_option
    if 'remove' in text:
        bot.send_message(message.chat.id, "You are not tracking any shipments. Start by using the command /track")    
    
    #modify_option
    if 'modify' in text:
        bot.send_message(message.chat.id, "You are not tracking any shipments. Start by using the command /track")
    
    #help_option
    if 'help' in text:
        bot.send_message(message.chat.id, "⚙️ Commands :")
    
    else:
        bot.send_message(message.chat.id, "❗ I don't understand. Please try again!")

def trackid_handler(message):
    track_id = message.text
    if len(track_id) > 30:
        bot.send_message(message.chat.id, "Tracking number cannot be longer than 30 characters. Try again!") 

#CancelCommand

@bot.message_handler(commands=['cancel'])
def cancel(message):
    bot.send_message(message.chat.id, "👍 Cancelled. If you are having any issues, take a look at the help page.")


'''
#ListShipments

#@bot.message_handler(content_types=['text'])
#def list_shipment(message):
    text = message.text.lower()
    if 'list' in text:
        bot.send_message(message.chat.id, "You are not tracking any shipments. Start by using the command /track")
        
    #else:
        #bot.send_message(message.chat.id, "❗ I don't understand. Please try again!")

#RemoveShipments

@bot.message_handler(content_types=['text'])
def remove_shipment(message):
    text = message.text.lower()
    if 'remove' in text:
        bot.send_message(message.chat.id, "You are not tracking any shipments. Start by using the command /track")
    #else:
        #bot.send_message(message.chat.id, "❗ I don't understand. Please try again!")

#ModifyShipments

@bot.message_handler(content_types=['text'])
def modify_shipment(message):
    text = message.text.lower()
    if 'modify' in text:
        bot.send_message(message.chat.id, "You are not tracking any shipments. Start by using the command /track")
    #else:
        #bot.send_message(message.chat.id, "❗ I don't understand. Please try again!")

#Help command

@bot.message_handler(content_types=['text'])
def help(message):
    text = message.text.lower()
    if 'help' in text:
        bot.send_message(message.chat.id, "⚙️ Commands :")
        
    #else:
        #bot.send_message(message.chat.id, "❗ I don't understand. Please try again!")


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