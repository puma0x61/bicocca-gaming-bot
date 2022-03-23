#! usr/bin/python

import json
import sys

import telebot
from telebot import types

from core import *

### config
# reads bot token from config.json

config = json.load(open('../config.json'))
if config[sys.argv[1]]:
    bot = telebot.TeleBot(token=config[sys.argv[1]])
else:
    print("###################################################")
    print("# Please setup the needed keys in the config file #")
    print("###################################################")
    sys.exit()


@bot.message_handler(func=lambda message: message.from_user.is_bot != 'True', content_types=['new_chat_members'])
def handle_join(message):
    try:
        chat_id = message.chat.id
        private_id = message.from_user.id
        chat_name = message.chat.title
        if message.from_user.username is None:
            name = message.from_user.first_name
        else:
            name = '@' + message.from_user.username
        welcome_message = f'Ciao {name}! benvenutə su {chat_name}!\n' \
                          f'Qui potrai parlare di gaming e gioco di ruolo e fare amicizia con altri giocatori.\n\n' \
                          f'Dicci qualcosa di te, a cosa giochi?'
        buttons = [[types.InlineKeyboardButton('Regolamento e link', url='http://t.me/bicocca_gaming_bot')]]
        bot.send_message(chat_id, welcome_message, parse_mode='HTML', reply_markup=types.InlineKeyboardMarkup(buttons))
        bot.send_message(private_id, 'test')
    except Exception as e:
        print(e)
    pass


@bot.message_handler(func=lambda message: message.chat.type == 'private', commands=['start', 'help'])
def handle_start(message):
    try:
        chat_id = message.chat.id
        bot.send_message(chat_id, RULES)
        bot.send_message(chat_id, LINK_MESSAGE)
    except Exception as e:
        print(e)
    pass


bot.polling()
