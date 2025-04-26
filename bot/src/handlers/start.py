import telebot.types
from telebot import TeleBot


def start_handler(bot: TeleBot):
    @bot.message_handler(commands=['start'])
    def handle_start(message: telebot.types.Message):
        bot.send_message(message.chat.id,
                         "👋 Olá! Eu sou o Bot da FURIA.\nUse /resumo, /proximos, /resultados, /elenco e muito mais!")
