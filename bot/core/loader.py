from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.base import DefaultKeyBuilder
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio import Redis, ConnectionPool

from bot.core.config import settings

bot = Bot(token=settings.BOT_TOKEN, efault=DefaultBotProperties(parse_mode=ParseMode.HTML))

redis = Redis(
    connection_pool=ConnectionPool(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        db=0
    )
)
storage = RedisStorage(
    redis=redis,
    key_builder=DefaultKeyBuilder(with_bot_id=True)
)

dp = Dispatcher(storage=storage)
