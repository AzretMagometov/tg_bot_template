import logging

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State, default_state
from aiogram.types import Message

router = Router(name='main')

logger = logging.getLogger(__name__)


class OuterGroup(StatesGroup):
    inner_state_1 = State()
    inner_state_2 = State()


class DummyState(StatesGroup):
    start_state = State()
    outer_group = OuterGroup
    end_state = State()


@router.message(F.text, default_state)
@router.message(F.text, DummyState.end_state)
async def on_text_message(message: Message, state: FSMContext) -> None:
    await state.set_state(DummyState.start_state)
    _state = await state.get_state()

    await message.answer(_state)


@router.message(F.text, DummyState.start_state)
async def on_text_message(message: Message, state: FSMContext) -> None:
    await state.set_state(DummyState.outer_group.inner_state_1)
    _state = await state.get_state()

    await message.answer(_state)


@router.message(F.text, DummyState.outer_group.inner_state_1)
async def on_text_message(message: Message, state: FSMContext) -> None:
    await state.set_state(DummyState.outer_group.inner_state_2)
    _state = await state.get_state()

    await message.answer(_state)


@router.message(F.text, DummyState.outer_group.inner_state_2)
async def on_text_message(message: Message, state: FSMContext) -> None:
    await state.set_state(DummyState.end_state)
    _state = await state.get_state()

    await message.answer(_state)
