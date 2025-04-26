from src.services.api_client import get_summary


def resumo_handler(bot):
    @bot.message_handler(commands=["resumo"])
    def send_summary(message):
        summary = get_summary()
        best_maps = sorted(summary.maps, key=lambda m: (m.winRate * m.played), reverse=True)[:3]
        msg = f"""
🇧🇷 {summary.info.name} (Rank #{summary.ranking.current})
Coach: {summary.coach.name}
Instagram: {summary.info.instagram}

📊 Estatísticas da Fúria:
- {summary.stats.mapsPlayed} mapas jogados
- {summary.stats.wins} vitórias
- K/D Ratio: {summary.stats.kdRatio}

🔥 Mapas fortes:
{best_maps[0].name} ({best_maps[0].winRate}% de vitórias)
{best_maps[1].name} ({best_maps[1].winRate}% de vitórias)
{best_maps[2].name} ({best_maps[2].winRate}% de vitórias)
"""
        bot.reply_to(message, msg.strip())
