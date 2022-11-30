import telebot
from telebot import types
import operations_rational as op
import calculatortype as ty
import operations_complex as opCom
BOT_TOKEN = '5833580554:AAEg8Mf3Z4Qq435yzjzlnWEM2dGuGMja5zw' 
BOT_NAME = 'calc_paul' 
bot = telebot.TeleBot('5833580554:AAEg8Mf3Z4Qq435yzjzlnWEM2dGuGMja5zw')


bot = telebot.TeleBot("YOUR_BOT_TOKEN")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "привет, напиши выражение?")

bot.infinity_polling()



