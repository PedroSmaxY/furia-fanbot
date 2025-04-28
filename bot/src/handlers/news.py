from telebot import TeleBot, types
from src.services.api_client import get_news


def news_handler(bot: TeleBot):
    @bot.message_handler(commands=['news', 'noticias'])
    def handle_news(message: types.Message):
        news_data = get_news()

        msg = "*📰 Últimas Notícias da FURIA*\n\n"

        if news_data.total > 0:
            for i, news in enumerate(news_data.news, 1):
                msg += f"{i}. [{news.name}]({news.link})\n\n"
        else:
            msg += "Não há notícias recentes para mostrar.\n"

        msg += "_Fonte: HLTV.org_"

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🏠 Voltar ao Menu Principal", callback_data="cmd_start"))

        bot.send_message(
            message.chat.id,
            msg.strip(),
            parse_mode="Markdown",
            reply_markup=markup,
            disable_web_page_preview=False
        )
