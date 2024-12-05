import os
import telebot
from telebot import types
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

bot = telebot.TeleBot(API_KEY)

# List_Shipments
def list_shipment(message):
    bot.send_message(message.chat.id, "You are not tracking any shipments. Start by using the command /track")

# Remove_Shipments
def remove_shipment(message):
    bot.send_message(message.chat.id, "You are not tracking any shipments. Start by using the command /track")

# Share_Shipment
def share_shipment(message):
    bot.send_message(message.chat.id, "You are not tracking any shipments. Start by using the command /track")

# Modify_Shipments
def modify_shipment(message):
    bot.send_message(message.chat.id, "You are not tracking any shipments. Start by using the command /track")

# Help_Command
def help(message):
    bot.send_message(message.chat.id, "\u2699\ufe0f Commands :\n\n• /list - Show the list of shipments you are tracking.\n• /track - Track a new shipment.\n• /remove - Remove a shipment from database.\n• /modify - Modify a shipment.\n• /cancel - Cancel the current command.")

# Cancel_Command
def cancel(message):
    bot.send_message(message.chat.id, "\ud83d\udc4d Cancelled. If you are having any issues, take a look at /help")

# Track_Shipment
def track_shipment(message):
    bot.send_message(message.chat.id, "Please enter the tracking number of the shipment you'd like to track.")

# Start_Command
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    list_btn = types.KeyboardButton('/list')
    track_btn = types.KeyboardButton('/track')
    remove_btn = types.KeyboardButton('/remove')
    modify_btn = types.KeyboardButton('/modify')
    help_btn = types.KeyboardButton('/help')
    cancel_btn = types.KeyboardButton('/cancel')
    markup.add(list_btn, track_btn, remove_btn, modify_btn, help_btn, cancel_btn)
    bot.send_message(message.chat.id, "Welcome to UTrackBot! How can I assist you today?", reply_markup=markup)

# Button Handling
@bot.message_handler(commands=['start'])
def handle_start(message):
    start(message)

@bot.message_handler(commands=['list'])
def handle_list(message):
    list_shipment(message)

@bot.message_handler(commands=['remove'])
def handle_remove(message):
    remove_shipment(message)

@bot.message_handler(commands=['share'])
def handle_share(message):
    share_shipment(message)

@bot.message_handler(commands=['modify'])
def handle_modify(message):
    modify_shipment(message)

@bot.message_handler(commands=['help'])
def handle_help(message):
    help(message)

@bot.message_handler(commands=['cancel'])
def handle_cancel(message):
    cancel(message)

@bot.message_handler(commands=['track'])
def handle_track(message):
    track_shipment(message)

if __name__ == '__main__':
    bot.polling(none_stop=True)
