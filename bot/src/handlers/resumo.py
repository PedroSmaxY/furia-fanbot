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

        msg = "*🏴 FURIA eSports — #" + str(summary.ranking.current) + " no ranking mundial*\n\n"

        msg += "*📊 Estatísticas Gerais:*\n"
        msg += "• 🗺️ " + str(summary.stats.mapsPlayed) + " mapas jogados\n"
        msg += "• 🏆 " + str(summary.stats.wins) + " vitórias\n"
        msg += "• ⚔️ K/D Ratio: " + f"{summary.stats.kdRatio:.2f}\n\n"

        msg += "*🔥 Top Mapas:*\n"
        for i, m in enumerate(best_maps, 1):
            win_rate = f"{m.winRate:.1f}" if isinstance(m.winRate, float) else m.winRate
            msg += "• " + str(i) + ". " + m.name.capitalize() + " — " + str(win_rate) + "% de vitórias\n"

        msg += "\n*🏅 Últimas Conquistas:*\n"
        if recent_achievements:
            for achievement in recent_achievements:
                msg += "• " + achievement.event.name.capitalize() + "\n"
        else:
            msg += "• Sem conquistas recentes\n"

        msg += "\n_Use /info para ver as redes sociais e contatos da FURIA_"

        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(
            types.InlineKeyboardButton("ℹ️ Informações", callback_data="cmd_info"),
            types.InlineKeyboardButton("🏠 Menu Principal", callback_data="cmd_start")
        )

        bot.send_message(
            message.chat.id,
            msg.strip(),
            parse_mode="Markdown",
            reply_markup=markup,
            disable_web_page_preview=True,
        )
