from telebot import TeleBot, types
from src.services.api_client import get_summary


def resumo_handler(bot: TeleBot):
    @bot.message_handler(commands=['resumo', 'resume', 'stats'])
    def send_summary(message: types.Message):

        summary = get_summary()

        best_maps = sorted(
            summary.maps,
            key=lambda map_element: (map_element.winRate * map_element.played),
            reverse=True
        )[:3]

        recent_achievements = summary.achievements[:3]

        msg = f"""
*🏴 FURIA eSports — #{summary.ranking.current} no ranking mundial*

🖥️ [Site oficial](https://www.furia.gg/)
📱 [Contato WhatsApp](https://wa.me/5511993404466)

*📸 Redes sociais:*
• [Instagram]({summary.info.instagram})
• [Facebook](https://www.facebook.com/furiagg)
• [TikTok](https://www.tiktok.com/@furiagg)
• [Youtube](https://www.youtube.com/@FURIAgg)
• [Twitch](https://www.twitch.tv/furiatv)
• [X](https://x.com/FURIA)

*📊 Estatísticas Gerais:*
• 🗺️ {summary.stats.mapsPlayed} mapas jogados
• 🏆 {summary.stats.wins} vitórias
• ⚔️ K/D Ratio: {summary.stats.kdRatio:.2f}

*🔥 Top Mapas:*"""

        for i, m in enumerate(best_maps, 1):
            win_rate = f"{m.winRate:.1f}" if isinstance(m.winRate, float) else m.winRate
            msg += f"\n• {i}. {m.name.capitalize()} — {win_rate}% de vitórias"

        msg += "\n\n*🏅 Últimas Conquistas:*"

        if recent_achievements:
            for achievement in recent_achievements:
                msg += f"\n• {achievement.event.name.capitalize()}"
        else:
            msg += "\n• Sem conquistas recentes"

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🏠 Voltar ao Menu Principal", callback_data="cmd_start"))

        bot.send_message(
            message.chat.id,
            msg.strip(),
            parse_mode="Markdown",
            reply_markup=markup,
            disable_web_page_preview=True,
        )
