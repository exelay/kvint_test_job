from typing import Dict

from telebot import TeleBot
from telebot.types import Message

from transitions.core import MachineError

from core import PizzaOrder
from settings import TELEGRAM_BOT_TOKEN, DEFAULT_ANSWER, DIALOG_TOKENS


bot = TeleBot(TELEGRAM_BOT_TOKEN)

orders: Dict[int, PizzaOrder] = {}


def get_or_create_order(user_id: int) -> PizzaOrder:
    order = orders.get(user_id)

    if not order:
        order = PizzaOrder()
        orders[user_id] = order

    return order


@bot.message_handler(commands=['start'])
def start_message_handler(message: Message) -> None:
    user_id = message.from_user.id
    chat_id = message.chat.id
    order = get_or_create_order(user_id)
    text = order.message
    bot.send_message(chat_id, text)


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
    if any(token in message.text.lower() for token in DIALOG_TOKENS['starting_order']):
        order.start_order()
        answer = order.message
    elif any(token in message.text.lower() for token in DIALOG_TOKENS['big']):
        order.select_big_pizza()
        answer = order.message
    elif any(token in message.text.lower() for token in DIALOG_TOKENS['small']):
        order.select_small_pizza()
        answer = order.message
    elif any(token in message.text.lower() for token in DIALOG_TOKENS['cash']):
        order.select_cash_payment()
        answer = order.message
    elif any(token in message.text.lower() for token in DIALOG_TOKENS['card']):
        order.select_card_payment()
        answer = order.message
    elif any(token in message.text.lower() for token in DIALOG_TOKENS['confirm']):
        order.confirm_order()
        answer = order.message
        order.cleanse_order()
    elif any(token in message.text.lower() for token in DIALOG_TOKENS['decline']):
        order.decline_order()
        answer = order.message
        order.cleanse_order()
    else:
        answer = DEFAULT_ANSWER

    return answer
