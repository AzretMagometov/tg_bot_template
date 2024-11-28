from httpx import AsyncClient
from openai import AsyncOpenAI, NotGiven, NOT_GIVEN
from openai.types.beta import Assistant, Thread
from openai.types.beta.threads import Run

from bot.core.config import settings

client = AsyncOpenAI(
    http_client=AsyncClient(proxy=settings.proxy)
)


async def get_assistant(assistant_id: str) -> Assistant:
    return await client.beta.assistants.retrieve(assistant_id)


async def create_thread(user_id: int) -> Thread:
    return await client.beta.threads.create(metadata={"user_id": user_id})


async def add_user_message(thread_id: str, content: str) -> None:
    await client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=content
    )


async def start_run(assistant_id: str, thread_id: str, additional_instructions: str | NotGiven = NOT_GIVEN) -> Run:
    return await client.beta.threads.runs.create_and_poll(
        assistant_id=assistant_id,
        thread_id=thread_id,
        additional_instructions=additional_instructions
    )
