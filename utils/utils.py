# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
@Author: MojtabaMonfared
All Right Reserved
2010-2016 MojtabaMonfared
Under GNU AGPL v3 2016*
Available on Github*
"""

import telebot
import telpot
import sys
import os
import json
import re
import platform
import requests
import random
import string
import logging
from telebot import types
from utils import *

botToken = ''
bot = telebot.TeleBot(botToken)

sudo = 132640720
bot_id = bot.get_me().id
log = '@BuildTwistLog'

log_kb = types.InlineKeyboardMarkup()
log_kb.add(types.InlineKeyboardButton("Bot", url='https://telegram.me/BuildTwistBot'))
log_kb.add(types.InlineKeyboardButton("Website", url=''))
log_kb.add(types.InlineKeyboardButton("Rate Bot", url=''))


kb = types.ReplyKeyboardMarkup()
kb.row(types.ReplyKeyboardButton("Add Bot", resize_keyboard=True))
kb.row(types.ReplyKeyboardButton("Setting", resize_keyboard=True), types.ReplyKeyboardButton("Manage Bots"))
kb.row(types.ReplyKeyboardButton("Documention", resize_keyboard=True))

user_dict = {}

class user:
	def __init__(self, name):
		self.name = name
		self.token = None
		self.bot = None
		self.stats = None

with open('response.json') as f:
    response = json.load(f, object_pairs_hook=OrderedDict)

with open('user.json') as f:
	userload = json.load(f, object_pairs_hook=OrderedDict)

with open('bb.json') as f:
	blacklist = json.load(f, object_pairs_hook=OrderedDict)

with open('chat.json') as f:
	chatlist = json.load(f, object_pairs_hook=OrderedDict)

def is_sudo(message.from_user.id):
	sudo = 132640720
	return message.from_user.id == sudo