import os
import telebot

API_TOKEN = os.getenv("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Это Модный Сейлер. Введи название товара и его цену.")

bot.polling()