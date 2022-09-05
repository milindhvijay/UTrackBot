import os
import telebot
from buttonmenu import *
from dotenv import load_dotenv
from aftership.lastcheckpoint import last_checkpoint_func

load_dotenv()

BOT_API_KEY = os.getenv('BOT_API_KEY')

bot = telebot.TeleBot(BOT_API_KEY)


def trackings():
    @bot.message_handler(content_types=['text'])
    def button_menu(message):
        text = message.text.lower()

        # track_option
        if 'track' in text:
            # tracking_shipment(message)
            track_shipment = bot.send_message(
                message.chat.id, "📦 I'm ready. Enter your tracking number :\n\n/cancel".format(message.from_user, bot.get_me()))
            bot.register_next_step_handler(track_shipment, trackid_handler)

        # list_option
        elif 'list' in text:
            list_shipment(message)

        # remove_option
        elif 'remove' in text:
            remove_shipment(message)

        # share_option
        elif 'share' in text:
            share_shipment(message)

        # modify_option
        elif 'modify' in text:
            modify_shipment(message)

        # help_option
        elif 'help' in text:
            help(message)

        # cancel_command
        elif 'cancel' in text:
            cancel(message)

        else:
            bot.send_message(
                message.chat.id, "❗ I don't understand. Please try again!")

    # Tracking_number_exception

    def trackid_handler(message):
        track_number = message.text
        if 'cancel' in track_number:
            cancel(message)
        elif len(track_number) > 30:
            bot.send_message(
                message.chat.id, "❗Tracking number cannot be longer than 30 characters. Try again!")
        else:
            bot.send_message(message.chat.id, last_checkpoint_func(
                message=message, city=message)
            )

    bot.polling()
