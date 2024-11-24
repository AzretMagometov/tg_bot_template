from aiogram import Router


def get_handlers_router() -> Router:
    from . import menu, start, main

    router = Router()
    router.include_routers(
        start.router,
        menu.router,
        main.router
    )

    return router
