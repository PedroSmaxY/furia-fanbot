from src.services.api_client import get_summary


def resumo_handler(bot):
    @bot.message_handler(commands=["resumo"])
    def send_summary(message):
        data = get_summary()['summary']

        info = data["info"]
        coach = data["coach"]
        stats = data["stats"]
        top_maps = ", ".join(map["name"].capitalize() for map in data["maps"][:3])

        msg = f"""
🇧🇷 {info['name']} (Rank #{data['ranking']['current']})
Coach: {coach['name']}
Instagram: {info['instagram']}

📊 Estatísticas:
- {stats['mapsPlayed']} mapas jogados
- {stats['wins']} vitórias
- K/D Ratio: {stats['kdRatio']}

🔥 Mapas fortes:
{top_maps}
"""
        bot.reply_to(message, msg.strip())
