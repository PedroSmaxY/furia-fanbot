from dotenv import load_dotenv
import telebot
from os import getenv

load_dotenv()

API_KEY = getenv("API_KEY")

bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     "Hello! I'm a bot that can help you with various tasks. Type /help to see what I can do.")
    print(f"User {message.from_user.username} started the bot.")


print("Bot is running...")
bot.infinity_polling()
print("Bot has stopped.")
