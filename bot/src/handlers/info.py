from telebot import TeleBot, types
from src.services.api_client import get_summary


def info_handler(bot: TeleBot):
    @bot.message_handler(commands=['info', 'informacoes', 'sobre'])
    def handle_info(message: types.Message):
        summary = get_summary()

        msg = "*ℹ️ Informações sobre a FURIA eSports*\n\n"

        msg += "*🏴 Sobre:*\n"
        msg += "A FURIA é uma organização brasileira de esports fundada em 2017, que compete em diversos jogos como CS:GO, Valorant, Rainbow Six, entre outros.\n\n"

        msg += "*🌍 Localização:*\n"
        msg += "• Sede principal: São Paulo, Brasil\n"
        msg += "• Centro de treinamento na América do Norte\n\n"

        msg += "*🏆 Conquistas gerais:*\n"
        msg += "• #" + str(summary.ranking.current) + " no ranking mundial\n"
        msg += "• " + str(len(summary.achievements)) + " conquistas registradas\n"
        msg += "• " + str(summary.stats.wins) + " vitórias em " + str(summary.stats.mapsPlayed) + " mapas jogados\n\n"

        msg += "*💰 Patrocinadores:*\n"
        msg += "• Adidas\n"
        msg += "• Cruzeiro do Sul\n"
        msg += "• Lenovo\n"
        msg += "• PokerStars\n"
        msg += "• Red Bull\n"
        msg += "• Hellmann's\n\n"

        msg += "*📱 Contato e redes:*\n"
        msg += "• Site: [www.furia.gg](https://www.furia.gg/)\n"
        msg += "• WhatsApp: [Contato Inteligente](https://wa.me/5511993404466) (Closed Beta)\n"
        msg += "• Instagram: [" + summary.info.instagram.replace("https://www.",
                                                                 "") + "](" + summary.info.instagram + ")\n"
        msg += "• Facebook: [facebook.com/furiagg](https://www.facebook.com/furiagg)\n"
        msg += "• TikTok: [tiktok.com/@furiagg](https://www.tiktok.com/@furiagg)\n"
        msg += "• YouTube: [youtube.com/@FURIAgg](https://www.youtube.com/@FURIAgg)\n"
        msg += "• Twitch: [twitch.tv/furiatv](https://www.twitch.tv/furiatv)\n"
        msg += "• X: [x.com/FURIA](https://x.com/FURIA)\n\n"

        msg += "*Use /elenco para ver os jogadores atuais da equipe*"

        team_logo = "https://apiesltv.imgix.net/images/team/logo/180_6389fd40-d1b3-4bd3-9a64-6ede7e24bd38.png?auto=compress&w=400"

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🏠 Voltar ao Menu Principal", callback_data="cmd_start"))

        bot.send_photo(
            chat_id=message.chat.id,
            photo=team_logo,
            caption=msg.strip(),
            parse_mode="Markdown",
            reply_markup=markup,
        )
