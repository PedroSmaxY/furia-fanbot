from telebot import TeleBot, types
from src.services.api_client import get_summary


def info_handler(bot: TeleBot):
    @bot.message_handler(commands=['info', 'informacoes', 'sobre'])
    def handle_info(message: types.Message):
        summary = get_summary()

        msg = f"""
*ℹ️ Informações sobre a FURIA eSports*

*🏴 Sobre:*
A FURIA é uma organização brasileira de esports fundada em 2017, que compete em diversos jogos como CS:GO, Valorant, Rainbow Six, entre outros.

*🌍 Localização:*
• Sede principal: São Paulo, Brasil
• Centro de treinamento na América do Norte

*🏆 Conquistas gerais:*
• #{summary.ranking.current} no ranking mundial
• {len(summary.achievements)} conquistas registradas
• {summary.stats.wins} vitórias em {summary.stats.mapsPlayed} mapas jogados

*💰 Patrocinadores:*
• Adidas
• Cruzeiro do Sul
• Lenovo
• PokerStars
• Red Bull
• Hellmann's

*📱 Contato e redes:*
• Site: [www.furia.gg](https://www.furia.gg/)
• Instagram: [{summary.info.instagram.replace("https://www.", "")}]({summary.info.instagram})
• Facebook: [facebook.com/furiagg](https://www.facebook.com/furiagg)
• TikTok: [tiktok.com/@furiagg](https://www.tiktok.com/@furiagg)
• YouTube: [youtube.com/@FURIAgg](https://www.youtube.com/@FURIAgg)
• Twitch: [twitch.tv/furiatv](https://www.twitch.tv/furiatv)
• X: [x.com/FURIA](https://x.com/FURIA)

*Use /elenco para ver os jogadores atuais da equipe*
"""

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🏠 Voltar ao Menu Principal", callback_data="cmd_start"))

        bot.send_message(
            message.chat.id,
            msg.strip(),
            parse_mode="Markdown",
            reply_markup=markup,
            disable_web_page_preview=True,
        )
