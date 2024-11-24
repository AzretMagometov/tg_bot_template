from aiogram import Dispatcher, Bot

from bot.core.config import main_config

dp = Dispatcher()

bot = Bot(token=main_config.tg_token)
