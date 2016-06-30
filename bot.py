# -*- coding: utf-8 -*-
"""
@Author: MojtabaMonfared
All Right Reserved
2010-2016 MojtabaMonfared
Under GNU AGPL v3 2016*
Available on Github*
"""

from utils import utils
import os
import sys


if sys.version_info.major > 2.7:
    raise Exception("Must be using Python 2.7.6")

try:
	bot.send_message(132640720, "*BuildTwist Runned!*", reply_markup=sudo_kb, parse_mode="Markdown")
except Exception as e:
	bot.send_message(132640720, "`" + str(e) + "`", parse_mode="Markdown")


@bot.message_handler(commands=['start'])
def start_text(message):
	cid = message.chat.id
	uid = message.from_user.id
	name = message.from_user.first_name
	if uid not in loadjson("user"):
		addUser(uid, message.from_user.first_name, "user")
		bot.send_message(cid, response['start_new'], parse_mode="Markdown", reply_markup=kb, disable_web_page_preview=True)
	else:
		bot.send_message(cid, response['start'], parse_mode="Markdown", reply_markup=kb, disable_web_page_preview=True)

@bot.message_handler(commands=['help'])
def help_text(message):
	bot.send_message(message.chat.id, response['help'].format(*****), parse_mode="Markdown")

@bot.message_handler(func=lambda message: True)
def add_bot(message):
	if message.text == "Add Bot":
		msg = bot.send_message(message.chat.id, "Send Me Token", reply_markup=types.ForceReply(selective=True))
		bot.register_next_step_handler(msg, process_token_handler)
	except:
		logging.error('Somthing went Wrong')
		bot.reply_to(message, 'OooOooOps\n    O_o')

def process_token_handler(message):
	user.token = token
	check = re.search(r'[\d]{9}:AAH.+', message.text).group()
	if check in message.text:
		os.system("python home\bots\1\bot.py {}".format(check))
		try:
			token = check
			bot_reg = telebot.TeleBot(token)
			bot_reg_name = bot_reg.get_me().username
			bot_reg_firstname = bot_reg.get_me().first_name
			bot.send_message(message.chat.id, "Bot %s \n@%s\nWas Added\n\n_Go in [Pv](https://telegram.me/%s) and Send /start" % (bot_reg_firstname, bot_reg_name, bot_reg_name), parse_mode="Markdown", reply_markup=kb, disable_web_page_preview=True)
		except:
			bot.reply_to(message, "Somthing went Wrong")
	else:
		bot.reply_to(message, "Send Correct Token")


@bot.message_handler(commands=['log'])
def send_log(message):
	cid = message.chat.id
	uid = message.from_user.id
	if is_sudo(uid):
		msg = bot.send_message(cid, "_Send Your Message Sudo_♥\n*Note;*\nit Will Sent To `@BuildTwistLog`", parse_mode="Markdown", reply_markup=types.ForceReply(selective=True))
		bot.register_next_step_handler(msg, process_log_message)
	else:
		bot.reply_to(message, "`Just For` *Sudo*", parse_mode="Markdown")

def process_log_message(message):
	text = message.text
	bot.send_message(log, text, parse_mode="Markdown", disable_web_page_preview=False, reply_markup=log_kb)

@bot.message_handler(commands=['bitly'])
def bitly(message):
	uid = message.from_user.id
	cid = message.chat.id
	if is_sudo(message.from_user.id):
	    text = message.text.split(' ')[1]
	    url = 'https://api-ssl.bitly.com/v3/shorten'
	    params = {
	        'access_token': 'f94d249d269f5ae4af107d9fdfddd36a6a88327e',
	        'longUrl': text,
	    }
	    jstr = requests.get(url, params=params, headers=None, files=None, data=None)       
	    data = json.loads(jstr.text)
	    tex = data['data']['url']
	    bot.send_message(cid, tex)
	else:
		bot.reply_to(message, "`Just For` *Sudo*", parse_mode="Markdown")




bot.polling(none_stop=True)

#  MojtabaMonfared