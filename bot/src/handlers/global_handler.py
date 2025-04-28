from telebot import TeleBot

from src.handlers.info import info_handler
from src.handlers.match_notification import match_notifications_handler
from src.handlers.matches import matches_handler
from src.handlers.news import news_handler
from src.handlers.next_matches import next_matches_handler
from src.handlers.players import players_handler
from src.handlers.resumo import resumo_handler
from src.handlers.start import start_handler


def set_handlers(bot: TeleBot):
    start_handler(bot)
    resumo_handler(bot)
    players_handler(bot)
    info_handler(bot)
    matches_handler(bot)
    next_matches_handler(bot)
    match_notifications_handler(bot)
    news_handler(bot)
