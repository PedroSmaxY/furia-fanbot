import telebot
from telebot import TeleBot

from src.services.api_client import get_roster


def players_handler(bot: TeleBot):
    @bot.message_handler(commands=['players'])
    def handle_players(message: telebot.types.Message):
        players = get_roster().players

        bot.send_message(message.chat.id,
                         f"👥 Elenco da FURIA:\n"
                         f"1. {players[0].name}\n"
                         f"2. {players[1].name}\n"
                         f"3. {players[2].name}\n"
                         f"4. {players[3].name}\n"
                         f"5. {players[4].name}\n")
