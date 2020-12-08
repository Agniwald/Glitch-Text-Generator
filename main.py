import telebot
from telebot import types
import generator
import os

from dotenv import load_dotenv
load_dotenv()

bot = telebot.TeleBot(os.environ.get("TOKEN"))


@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, "🌀 You can create your own z̮͈̍͒͆ͅạ͔̠̍̆̿l̖͚͕͂̄͝ĝ͔͉̠̭̍͒͗o̬͉̓͞ ̟̈́t̰̬̜̳̽̄͊̍ex̗͒ť̪ by easily entering your text.")


@bot.message_handler(content_types=['text'])
def zalgo(message):
	result = generator.zalgo(message.text)
	bot.reply_to(message, result)


if __name__ == '__main__':
	bot.infinity_polling()
