from telebot import TeleBot


def start(bot: TeleBot):
    @bot.message_handler(commands=['start'])
    def handle_start(message):
        bot.send_message(message.chat.id,
                         "👋 Olá! Eu sou o Bot da FURIA.\nUse /resumo, /proximos, /resultados, /elenco e muito mais!")
        print(f"User {message.from_user.username} started the bot.")
