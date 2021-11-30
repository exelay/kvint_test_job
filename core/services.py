from typing import Dict
from loguru import logger

from core.types import PizzaOrder


orders: Dict[int, PizzaOrder] = {}


def get_or_create_order(user_id: int) -> PizzaOrder:
    order = orders.get(user_id)

    if not order:
        order = PizzaOrder()
        orders[user_id] = order
        logger.debug(f'User {user_id} created order.')

    return order
