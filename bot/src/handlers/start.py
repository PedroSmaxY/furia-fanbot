import telebot.types
from telebot import TeleBot


def start_handler(bot: TeleBot):
    @bot.message_handler(commands=['start'])
    def handle_start(message: telebot.types.Message):
        team_logo = "https://apiesltv.imgix.net/images/team/logo/180_6389fd40-d1b3-4bd3-9a64-6ede7e24bd38.png?auto=compress&w=400"

        bot.send_photo(message.chat.id, team_logo,
                       "👋 Olá! Eu sou o Bot da FURIA.\nUse /resumo, /proximos, /resultados, /elenco e muito mais!")
