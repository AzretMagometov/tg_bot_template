import asyncio
import logging

from bot.core.loader import dp, bot
from bot.handlers import get_handlers_router
from utils.logging import setup_logging_base_config

setup_logging_base_config()
logger = logging.getLogger(__name__)


async def on_startup() -> None:
    logger.info("bot starting...")

    dp.include_router(get_handlers_router())

    logger.info((await bot.get_me()).model_dump_json(indent=4, exclude_none=True))

    logger.info("bot started...")


async def on_shutdown() -> None:
    logger.info("bot stopping...")

    await dp.storage.close()
    await dp.fsm.storage.close()

    await bot.delete_webhook()
    await bot.session.close()

    logger.info("bot stopped")


async def main():
    logger.info("---- BOT ENTRY POINT ----")

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
