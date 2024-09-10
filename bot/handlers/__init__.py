from bot.dispatcher import dp
from bot.handlers.main import main_router
from bot.handlers.payment import order_router

dp.include_routers(*[
    main_router,
    order_router
])
