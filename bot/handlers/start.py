from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router(name="start")


@router.message(CommandStart())
async def on_start_command(message: Message):
    await message.answer(f"hello, {message.from_user.first_name}")
