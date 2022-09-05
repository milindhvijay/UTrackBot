from email import message
import os
import types
import telebot
from telebot import types
from buttonmenu import *
from dotenv import load_dotenv
from aftership.lastcheckpoint import last_checkpoint_func
from greeting import greetings
from tracking import trackings

load_dotenv()

BOT_API_KEY = os.getenv('BOT_API_KEY')

bot = telebot.TeleBot(BOT_API_KEY)


# Greeting Message
greetings()

# Tracking
trackings()
