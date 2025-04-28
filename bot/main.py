from dotenv import load_dotenv
from telebot import TeleBot, types
from os import getenv

from src.handlers.global_handler import set_handlers
from src.handlers.match_notification import start_match_notification_scheduler

load_dotenv()

TELEGRAMBOT_KEY = getenv("TELEGRAMBOT_KEY")

bot = TeleBot(TELEGRAMBOT_KEY)

set_handlers(bot)
notification_thread = start_match_notification_scheduler(bot)


@bot.message_handler(func=lambda message: True)
def handle_unknown_messages(message: types.Message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("🏠 Voltar ao Menu Principal", callback_data="cmd_start")
    )

    bot.send_message(
        message.chat.id,
        "Desculpe, não reconheço este comando. Use os botões abaixo ou digite /start para ver as opções disponíveis.",
        reply_markup=markup,
        parse_mode="Markdown"
    )


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
