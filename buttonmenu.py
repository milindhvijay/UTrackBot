import telebot

API_KEY = '2074114916:AAGIMQ3J4whzLqmMMiTJqLtSNrgwrQdZ9_w'
bot = telebot.TeleBot(API_KEY)

#ListShipments
def list_shipment(message):    
    bot.send_message(message.chat.id, "You are not tracking any shipments. Start by using the command /track")   
    
#RemoveShipments
def remove_shipment(message):
    bot.send_message(message.chat.id, "You are not tracking any shipments. Start by using the command /track")
    
#ModifyShipments
def modify_shipment(message):
    bot.send_message(message.chat.id, "You are not tracking any shipments. Start by using the command /track")
    
#Help command
def help(message):
    bot.send_message(message.chat.id, "⚙️ Commands :")