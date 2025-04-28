from telebot import TeleBot

from src.services.api_client import get_summary


def resumo_handler(bot: TeleBot):
    @bot.message_handler(commands=['resumo', 'resume'])
    def send_summary(message):
        summary = get_summary()

        best_maps = sorted(summary.maps, key=lambda map_element: (map_element.winRate * map_element.played),
                           reverse=True)[
                    :3]

        lasts_achievements = summary.achievements[:3]

        msg = f"""
🏴 FURIA eSports — *#{summary.ranking.current} no ranking mundial*

🖥️ Site oficial - https://www.furia.gg/

📸 Redes sociais:
    - [Instagram]({summary.info.instagram})
    - [Facebook](https://www.facebook.com/furiagg)
    - [TikTok](https://www.tiktok.com/@furiagg)
    - [Youtube](https://www.youtube.com/@FURIAgg)
    - [Twitch](https://www.twitch.tv/furiatv)
    - [X](https://x.com/FURIA)

📊 *Estatísticas Gerais:*
- 🗺️ {summary.stats.mapsPlayed} mapas jogados
- 🏆 {summary.stats.wins} vitórias
- ⚔️ K/D Ratio: {summary.stats.kdRatio}

🔥 *Top Mapas:*
"""
        for m in best_maps[:3]:
            msg += f"- {m.name.capitalize()} — {m.winRate}% de vitórias\n"
        msg += f"""
🏅 *Últimas Conquistas:*
"""
        for achievement in lasts_achievements:
            msg += f"- {achievement.event.name.capitalize()} em 1º lugar\n"

        bot.send_message(
            message.chat.id,
            msg.strip(),
            parse_mode="Markdown",
            disable_web_page_preview=True,
        )
