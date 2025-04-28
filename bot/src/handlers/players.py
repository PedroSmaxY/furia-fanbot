from telebot import TeleBot, types
from src.services.api_client import get_roster


def players_handler(bot: TeleBot):
    @bot.message_handler(commands=['players', 'elenco'])
    def handle_players(message: types.Message):
        players = get_roster().players

        msg = "👥 *Elenco da FURIA*\n\n"

        msg += "🧩 *Titulares:*\n"
        for player in players:
            if player.type not in ['Benched', 'Coach']:
                msg += "   • " + player.name + "\n"

        msg += "\n👨‍🏫 *Coach:*\n"
        for player in players:
            if player.type == 'Coach':
                msg += "   • " + player.name + "\n"

        msg += "\n🛋️ *Reservas:*\n"
        for player in players:
            if player.type == 'Benched':
                msg += "   • " + player.name + "\n"

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🏠 Voltar ao Menu Principal", callback_data="cmd_start"))

        bot.send_message(
            message.chat.id,
            msg.strip(),
            reply_markup=markup,
            parse_mode='Markdown',
            disable_web_page_preview=True
        )
