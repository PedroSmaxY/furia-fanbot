from telebot import TeleBot, types
from src.services.pandascore_client import get_team
from src.services.api_client import get_roster


def players_handler(bot: TeleBot):
    @bot.message_handler(commands=['players', 'elenco'])
    def handle_players(message: types.Message):
        pandascore_team = get_team()
        pandascore_players = pandascore_team.players

        roster = get_roster()

        roster_by_name = {player.name.lower(): player for player in roster.players}
        roster_types = {player.name.lower(): player.type for player in roster.players}

        coach_types = ['Coach']
        active_types = ['Starter']
        benched_types = ['Benched']

        msg = "👥 *Elenco da FURIA*\n\n"

        msg += "🧩 *Titulares:*\n"
        titulares_mostrados = []

        for player in roster.players:
            if player.type in active_types:
                titulares_mostrados.append(player.name.lower())
                pandascore_player = next((p for p in pandascore_players if p.name.lower() == player.name.lower()), None)

                if pandascore_player:
                    msg += "   • *" + player.name + "* (" + pandascore_player.nationality + ") - "
                    msg += pandascore_player.first_name + " " + pandascore_player.last_name
                    if pandascore_player.age:
                        msg += " (" + str(pandascore_player.age) + " anos)"
                    msg += "\n"
                else:
                    msg += "   • *" + player.name + "*"
                    if hasattr(player, 'timeOnTeam'):
                        msg += " (" + player.timeOnTeam + " no time)"
                    msg += "\n"

        msg += "\n👨‍🏫 *Coach:*\n"
        coaches_mostrados = []

        for player in roster.players:
            if player.type in coach_types:
                coaches_mostrados.append(player.name.lower())
                pandascore_player = next((p for p in pandascore_players if p.name.lower() == player.name.lower()), None)

                if pandascore_player:
                    msg += "   • *" + player.name + "* - " + pandascore_player.first_name + " " + pandascore_player.last_name
                    if pandascore_player.age:
                        msg += " (" + str(pandascore_player.age) + " anos)"
                    msg += "\n"
                else:
                    msg += "   • *" + player.name + "*\n"

        msg += "\n🛋️ *Reservas:*\n"
        reservas_mostrados = []
        has_reserves = False

        for player in roster.players:
            if player.type in benched_types:
                has_reserves = True
                reservas_mostrados.append(player.name.lower())

                pandascore_player = next((p for p in pandascore_players if p.name.lower() == player.name.lower()), None)

                if pandascore_player:
                    msg += "   • *" + player.name + "* (" + pandascore_player.nationality + ") - "
                    msg += pandascore_player.first_name + " " + pandascore_player.last_name
                    if pandascore_player.age:
                        msg += " (" + str(pandascore_player.age) + " anos)"
                    msg += "\n"
                else:
                    msg += "   • *" + player.name + "*"
                    if hasattr(player, 'timeOnTeam'):
                        msg += " (" + player.timeOnTeam + " no time)"
                    msg += "\n"

        if not has_reserves:
            msg += "   • Sem jogadores reservas no momento\n"

        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(
            types.InlineKeyboardButton("🔄 Atualizar", callback_data="cmd_elenco"),
            types.InlineKeyboardButton("🏠 Menu Principal", callback_data="cmd_start")
        )

        bot.send_message(
            message.chat.id,
            msg.strip(),
            reply_markup=markup,
            parse_mode='Markdown',
            disable_web_page_preview=True
        )

    @bot.callback_query_handler(func=lambda call: call.data == "cmd_elenco")
    def callback_elenco(call):
        bot.delete_message(call.message.chat.id, call.message.message_id)
        handle_players(call.message)
