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
        chat_name = message.chat.title
        if message.from_user.username is None:
            name = message.from_user.first_name
        else:
            name = '@' + message.from_user.username
        welcome_message = f'Ciao {name}! benvenutə su {chat_name}!\n' + WELCOME_MESSAGE
        buttons = [[types.InlineKeyboardButton('Link vari', url='http://t.me/bicocca_gaming_bot')]]
        bot.send_message(chat_id, welcome_message, parse_mode='HTML', reply_markup=types.InlineKeyboardMarkup(buttons))
    except Exception as e:
        print(e)
    pass


@bot.message_handler(func=lambda message: message.chat.type == 'private', commands=['start', 'help'])
def handle_start(message):
    try:
        chat_id = message.chat.id
        bot.send_message(chat_id, LINK_MESSAGE, parse_mode='HTML')
    except Exception as e:
        print(e)
    pass


# @bot.message_handler(func=lambda message: message.chat.type == 'private', commands=['link'])
# def handle_start(message):
#     try:
#         chat_id = message.chat.id
#         bot.send_message(chat_id, LINK_MESSAGE, parse_mode='HTML')
#     except Exception as e:
#         print(e)
#     pass
#
#
# @bot.message_handler(func=lambda message: message.chat.type == 'private', commands=['rules'])
# def handle_start(message):
#     try:
#         chat_id = message.chat.id
#         bot.send_message(chat_id, RULES, parse_mode='HTML')
#     except Exception as e:
#         print(e)
#     pass


bot.polling()
