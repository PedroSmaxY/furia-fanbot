from telebot import TeleBot, types
from datetime import datetime
import pytz
from src.services.pandascore_client import get_future_matches


def format_date(date_str):
    if not date_str:
        return "Data não definida"

    match_date = datetime.fromisoformat(date_str.replace('Z', '+00:00'))

    br_tz = pytz.timezone('America/Sao_Paulo')
    match_date_br = match_date.astimezone(br_tz)

    return match_date_br.strftime("%d/%m/%Y %H:%M")


def next_matches_handler(bot: TeleBot):
    @bot.message_handler(commands=['next_matches', 'proximas_partidas', 'proximaspartidas'])
    def handle_next_matches(message: types.Message):
        match_list = get_future_matches("furia")

        msg = "*🎮 Próximas Partidas da FURIA*\n\n"

        if match_list.matches:
            for match in match_list.matches:
                if hasattr(match.videogame, 'slug') and match.videogame.slug in ['cs-go', 'cs2', 'counter-strike-2']:
                    match_date = format_date(match.begin_at)

                    opponent = "TBD"
                    for opp in match.opponents:
                        if hasattr(opp, 'opponent') and opp.opponent and opp.opponent.name != "FURIA":
                            opponent = opp.opponent.name
                            break

                    match_format = f"Bo{match.number_of_games}" if match.number_of_games else "TBD"

                    event_name = match.league.name
                    tournament_name = match.tournament.name if match.tournament else ""

                    msg += f"📅 *{match_date}*\n"
                    msg += f"🆚 *FURIA* vs *{opponent}*\n"
                    msg += f"🎲 Formato: {match_format}\n"
                    msg += f"🏆 Evento: {event_name}"
                    if tournament_name:
                        msg += f" - {tournament_name}"

                    if match.streams_list:
                        msg += "\n📺 Transmissões:"
                        for stream in match.streams_list:
                            if hasattr(stream, 'raw_url') and stream.raw_url:
                                stream_name = stream.raw_url.split('/')[-1]
                                msg += f" [{stream_name}]({stream.raw_url})"

                    msg += "\n\n"
        else:
            msg += "Não há partidas futuras agendadas no momento."

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🏠 Voltar ao Menu Principal", callback_data="cmd_start"))

        bot.send_message(
            message.chat.id,
            msg.strip(),
            parse_mode="Markdown",
            reply_markup=markup,
            disable_web_page_preview=True
        )
