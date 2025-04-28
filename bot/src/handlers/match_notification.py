import threading
import time
import json
import os
from datetime import datetime
import pytz
from telebot import TeleBot, types
from src.services.pandascore_client import get_future_matches

SUBSCRIBERS_FILE = 'data/match_subscribers.json'


def ensure_data_dir():
    os.makedirs('data', exist_ok=True)


def load_subscribers():
    ensure_data_dir()
    try:
        with open(SUBSCRIBERS_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_subscribers(subscribers):
    with open(SUBSCRIBERS_FILE, 'w') as file:
        json.dump(subscribers, file)


def load_known_matches():
    ensure_data_dir()
    try:
        with open('data/known_matches.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_known_matches(matches):
    with open('data/known_matches.json', 'w') as file:
        json.dump(matches, file)


def format_match_notification(match):
    br_tz = pytz.timezone('America/Sao_Paulo')
    match_date = datetime.fromisoformat(match.begin_at.replace('Z', '+00:00'))
    match_date_br = match_date.astimezone(br_tz)
    formatted_date = match_date_br.strftime("%d/%m/%Y %H:%M")

    opponent = "TBD"
    for opp in match.opponents:
        if hasattr(opp, 'opponent') and opp.opponent and opp.opponent.name != "FURIA":
            opponent = opp.opponent.name
            break

    event_name = match.league.name
    tournament_name = match.tournament.name if match.tournament else ""

    msg = f"*🚨 NOVA PARTIDA AGENDADA!* 🚨\n\n"
    msg += f"📅 *{formatted_date}*\n"
    msg += f"🆚 *FURIA* vs *{opponent}*\n"
    msg += f"🎲 Formato: Bo{match.number_of_games}\n"
    msg += f"🏆 Evento: {event_name}"
    if tournament_name:
        msg += f" - {tournament_name}"

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Ver todas as próximas partidas", callback_data="cmd_proximaspartidas"))

    return msg, markup


def check_for_new_matches(bot):
    print("Verificando novas partidas...")
    try:
        match_list = get_future_matches("furia")

        if not match_list or not match_list.matches:
            return

        known_matches = load_known_matches()
        new_matches = []

        for match in match_list.matches:
            if hasattr(match.videogame, 'slug') and match.videogame.slug in ['cs-go', 'cs2', 'counter-strike-2']:
                match_id = str(match.id)
                if match_id not in known_matches:
                    new_matches.append(match)
                    known_matches.append(match_id)

        save_known_matches(known_matches)

        if new_matches:
            subscribers = load_subscribers()
            for match in new_matches:
                msg, markup = format_match_notification(match)
                for chat_id in subscribers:
                    try:
                        bot.send_message(
                            chat_id,
                            msg,
                            parse_mode="Markdown",
                            reply_markup=markup,
                            disable_web_page_preview=True
                        )
                    except Exception as e:
                        print(f"Erro ao enviar notificação para {chat_id}: {e}")

            print(f"Enviadas notificações sobre {len(new_matches)} novas partidas")
    except Exception as e:
        print(f"Erro ao verificar novas partidas: {e}")


def start_match_notification_scheduler(bot):
    def scheduler_thread():
        while True:
            check_for_new_matches(bot)
            time.sleep(3600)

    thread = threading.Thread(target=scheduler_thread, daemon=True)
    thread.start()
    return thread


def match_notifications_handler(bot: TeleBot):
    @bot.message_handler(commands=['notificacoes', 'notifications'])
    def handle_notifications(message: types.Message):
        subscribers = load_subscribers()
        chat_id = str(message.chat.id)

        markup = types.InlineKeyboardMarkup(row_width=1)

        if chat_id in subscribers:
            markup.add(
                types.InlineKeyboardButton("❌ Desativar notificações", callback_data="notifications_off"),
                types.InlineKeyboardButton("🏠 Voltar ao Menu Principal", callback_data="cmd_start")
            )
            bot.send_message(
                message.chat.id,
                "*✅ Notificações ativadas*\n\nVocê receberá alertas quando novas partidas forem agendadas.",
                parse_mode="Markdown",
                reply_markup=markup
            )
        else:
            markup.add(
                types.InlineKeyboardButton("✅ Ativar notificações", callback_data="notifications_on"),
                types.InlineKeyboardButton("🏠 Voltar ao Menu Principal", callback_data="cmd_start")
            )
            bot.send_message(
                message.chat.id,
                "*❌ Notificações desativadas*\n\nVocê não está recebendo alertas de novas partidas.",
                parse_mode="Markdown",
                reply_markup=markup
            )

    @bot.callback_query_handler(func=lambda call: call.data in ["notifications_on", "notifications_off"])
    def handle_notification_callbacks(call):
        bot.answer_callback_query(call.id)
        chat_id = str(call.message.chat.id)
        subscribers = load_subscribers()

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🏠 Voltar ao Menu Principal", callback_data="cmd_start"))

        if call.data == "notifications_on":
            if chat_id not in subscribers:
                subscribers.append(chat_id)
                save_subscribers(subscribers)

            bot.edit_message_text(
                "*✅ Notificações ativadas com sucesso!*\n\nVocê receberá alertas quando novas partidas da FURIA forem agendadas.",
                call.message.chat.id,
                call.message.message_id,
                parse_mode="Markdown",
                reply_markup=markup
            )
        else:
            if chat_id in subscribers:
                subscribers.remove(chat_id)
                save_subscribers(subscribers)

            bot.edit_message_text(
                "*❌ Notificações desativadas com sucesso!*\n\nVocê não receberá mais alertas sobre novas partidas.",
                call.message.chat.id,
                call.message.message_id,
                parse_mode="Markdown",
                reply_markup=markup
            )
