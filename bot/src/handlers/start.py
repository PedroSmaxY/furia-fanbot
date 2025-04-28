import telebot.types
from telebot import TeleBot


def start_handler(bot: TeleBot):
    @bot.message_handler(commands=['start'])
    def handle_start(message: telebot.types.Message):
        team_logo = "https://apiesltv.imgix.net/images/team/logo/180_6389fd40-d1b3-4bd3-9a64-6ede7e24bd38.png?auto=compress&w=400"

        markup = telebot.types.InlineKeyboardMarkup(row_width=2)
        markup.add(
            telebot.types.InlineKeyboardButton("📊 Resumo", callback_data="cmd_resumo"),
            telebot.types.InlineKeyboardButton("👥 Elenco", callback_data="cmd_elenco"),
            telebot.types.InlineKeyboardButton("🎮 Partidas", callback_data="cmd_partidas"),
            telebot.types.InlineKeyboardButton("ℹ️ Informações", callback_data="cmd_info")
        )

        welcome_text = (
            "*🏆 BEM-VINDO AO BOT OFICIAL DA FURIA ESPORTS! 🏆*\n\n"
            "Acompanhe todas as informações, estatísticas e resultados "
            "da sua equipe brasileira favorita.\n\n"
            "*Comandos disponíveis:*\n"
            "• /resumo - Estatísticas gerais e conquistas\n"
            "• /elenco - Jogadores atuais da equipe\n"
            "• /partidas - Últimos resultados\n"
            "• /info - Informações sobre a organização\n\n"
            "Escolha uma opção abaixo ou digite um comando para começar:"
        )

        bot.send_photo(
            message.chat.id,
            team_logo,
            caption=welcome_text,
            reply_markup=markup,
            parse_mode="Markdown"
        )

    @bot.callback_query_handler(func=lambda call: call.data.startswith("cmd_"))
    def handle_command_buttons(call):
        bot.answer_callback_query(call.id)

        command = call.data[4:]

        if command == "start":
            handle_start(call.message)
            return

        command_map = {
            "resumo": "/resumo",
            "elenco": "/elenco",
            "partidas": "/partidas",
            "info": "/info"
        }

        if command in command_map:
            simulated_message = telebot.types.Message(
                message_id=call.message.message_id,
                from_user=call.from_user,
                date=call.message.date,
                chat=call.message.chat,
                content_type="text",
                options={},
                json_string=""
            )

            simulated_message.text = command_map[command]

            bot.process_new_messages([simulated_message])
