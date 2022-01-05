from loguru import logger

from telebot import TeleBot
from telebot.types import Message

from transitions.core import MachineError

from core.types import PizzaOrder
from core.services import get_or_create_order, orders
from core.settings import TELEGRAM_BOT_TOKEN, DEFAULT_ANSWER, DIALOG_TOKENS


bot = TeleBot(TELEGRAM_BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start_message_handler(message: Message) -> None:
    user_id = message.from_user.id
    chat_id = message.chat.id
    order = get_or_create_order(user_id)
    text = order.message
    bot.send_message(chat_id, text)
    logger.debug(f'User {user_id} ran the start command.')


@bot.message_handler()
def all_messages_handler(message: Message) -> None:
    user_id = message.from_user.id
    chat_id = message.chat.id
    order = orders.get(user_id)

    try:
        answer = get_answer(message, order)
    except MachineError:
        answer = DEFAULT_ANSWER

    bot.send_message(chat_id, answer)


def get_answer(message: Message, order: PizzaOrder) -> str:
    message_text = message.text.lower()
    user_id = message.from_user.id

    if any(token in message_text for token in DIALOG_TOKENS['starting_order']):
        order.start_order()
        answer = order.message
        logger.debug(f'User {message.from_user.id} started order.')
    elif any(token in message_text for token in DIALOG_TOKENS['big']):
        order.select_big_pizza()
        answer = order.message
        logger.debug(f'User {message.from_user.id} selected big pizza.')
    elif any(token in message_text for token in DIALOG_TOKENS['small']):
        order.select_small_pizza()
        answer = order.message
        logger.debug(f'User {message.from_user.id} selected small pizza.')
    elif any(token in message_text for token in DIALOG_TOKENS['cash']):
        order.select_cash_payment()
        answer = order.message
        logger.debug(f'User {message.from_user.id} selected cash payment.')
    elif any(token in message_text for token in DIALOG_TOKENS['card']):
        order.select_card_payment()
        answer = order.message
        logger.debug(f'User {message.from_user.id} selected card payment.')
    elif any(token in message_text for token in DIALOG_TOKENS['confirm']):
        order.confirm_order()
        answer = order.message
        order.clean_order()
        logger.debug(f'User {user_id} confirmed order.')
    elif any(token in message_text for token in DIALOG_TOKENS['decline']):
        order.decline_order()
        answer = order.message
        order.clean_order()
        logger.debug(f'User {user_id} declined order.')
    else:
        answer = DEFAULT_ANSWER

    return answer
