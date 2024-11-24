import os
from typing import Optional

from dotenv import load_dotenv, find_dotenv
from pydantic import BaseModel


class BotConfig(BaseModel):
    tg_token: str


def read_config_from_env(path: Optional[str] = None) -> BotConfig:
    if path:
        load_dotenv(path)
    else:
        load_dotenv(find_dotenv())

    return BotConfig(
        tg_token=os.getenv('TG_TOKEN')
    )


main_config = read_config_from_env()
