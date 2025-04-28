import telebot
from telebot import TeleBot

from src.services.api_client import get_roster


def players_handler(bot: TeleBot):
    @bot.message_handler(commands=['players', 'elenco'])
    def handle_players(message: telebot.types.Message):
        players = get_roster().players

        msg = f"""
👥 Elenco da FURIA:

🧩 **Titulares:**
"""
        for player in players:
            if player.type not in ['Benched', 'Coach']:
                msg += f"   • {player.name}\n"

        msg += f"""
👨‍🏫 *Coach:*
"""
        for player in players:
            if player.type == 'Coach':
                msg += f"   • {player.name}\n"

        msg += f"""
🛋️ *Reservas:*
"""
        for player in players:
            if player.type == 'Benched':
                msg += f"   • {player.name}\n"

        bot.send_message(message.chat.id, msg, parse_mode='Markdown')
