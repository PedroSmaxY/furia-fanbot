import telebot
from telebot import TeleBot


def players_handler(bot: TeleBot):
    @bot.message_handler(commands=['players'])
    def handle_players(message: telebot.types.Message):
        bot.send_message(message.chat.id,
                         "👥 Elenco da FURIA:\n"
                         "1. 🧑‍🦰 arT\n"
                         "2. 👨‍🦱 drop\n"
                         "3. 👨‍🦲 saffee\n"
                         "4. 👨‍🦳 yuurih\n"
                         "5. 👨‍🦰 jks\n")
