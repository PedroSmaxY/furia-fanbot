from telebot import TeleBot, types
from src.services.api_client import get_matches


def matches_handler(bot: TeleBot):
    @bot.message_handler(commands=['matches', 'partidas'])
    def handle_matches(message: types.Message):
        matches = get_matches()

        msg = "*🎮 Partidas Recentes da FURIA*\n\n"

        if matches.total > 0:
            for match in matches.matches:
                furia_score = match.score.split("-")[0]
                opponent_score = match.score.split("-")[1]

                if furia_score > opponent_score:
                    result_emoji = "✅"
                elif furia_score < opponent_score:
                    result_emoji = "❌"
                else:
                    result_emoji = "⚖️"

                # Formatar a mensagem para cada partida
                msg += f"*{match.date}* {result_emoji}\n"
                msg += f"🆚 *FURIA* vs *{match.opponent}*\n"
                msg += f"🗺️ Mapa: {match.map.capitalize()}\n"
                msg += f"📊 Placar: *{match.score}*\n"
                msg += f"🏆 Evento: {match.eventName}\n\n"
        else:
            msg += "Não há partidas recentes para mostrar."

        # Enviar a mensagem formatada
        bot.send_message(
            message.chat.id,
            msg.strip(),
            parse_mode="Markdown",
            disable_web_page_preview=True
        )
