import os
import telebot
from dotenv import load_dotenv

load_dotenv()

BOT_API_KEY = os.getenv('BOT_API_KEY')

bot = telebot.TeleBot(BOT_API_KEY)

#List_Shipments
def list_shipment(message):    
    bot.send_message(message.chat.id, "You are not tracking any shipments. Start by using the command /track")   
    
#Remove_Shipments
def remove_shipment(message):
    bot.send_message(message.chat.id, "You are not tracking any shipments. Start by using the command /track")

#Share_Shipment
def share_shipment(message):
    bot.send_message(message.chat.id, "You are not tracking any shipments. Start by using the command /track")
    
#Modify_Shipments
def modify_shipment(message):
    bot.send_message(message.chat.id, "You are not tracking any shipments. Start by using the command /track")
    
#Help_Command
def help(message):
    bot.send_message(message.chat.id, "⚙️ Commands :\n\n• /list - Show the list of shipments you are tracking.\n• /track - Track a new shipment.\n• /remove - Remove a shipment from database.\n• /modify - Modify a shipment.\n• /cancel - Cancel the current command.")

#Cancel_Command
def cancel(message):
    bot.send_message(message.chat.id, "👍 Cancelled. If you are having any issues, take a look at /help")    