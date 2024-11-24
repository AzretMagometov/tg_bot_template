from aiogram import Router


def get_handlers_router() -> Router:
    from . import menu, start

    router = Router()
    router.include_routers(
        start.router,
        menu.router
    )

    return router
