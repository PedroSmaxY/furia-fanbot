from dotenv import load_dotenv
import telebot
from os import getenv
from src.handlers.start import start

load_dotenv()

API_KEY = getenv("API_KEY")

bot = telebot.TeleBot(API_KEY)

start(bot)


def main():
    print("Bot is running...")
    try:
        bot.infinity_polling()
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        print("Bot has stopped.")


if __name__ == "__main__":
    main()
