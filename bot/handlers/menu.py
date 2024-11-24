from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router(name='menu')


@router.message(Command("menu"))
async def menu_handler(message: Message) -> None:
    await message.answer("add menu!")
