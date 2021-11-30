from loguru import logger
from environs import Env


env = Env()
env.read_env()

# Logging settings
logger.add('debug.log', format="{time} {level} {message}", level="DEBUG", rotation='100 KB', compression='zip')


# API Tokens
TELEGRAM_BOT_TOKEN = env.str('TELEGRAM_BOT_TOKEN')

# Dialog
DIALOG_TOKENS = {
    'starting_order': ("хочу", "заказ", "пиццу", "пиццы"),
    'big': ("большу", "бол"),
    'small': ("малую", "маленькую", "небольш"),
    'cash': ("налич", "налом"),
    'card': ("карт", "банк", "по карт"),
    'confirm': ("да", "ага", "ок"),
    'decline': ("неа", "нет"),
}

DEFAULT_ANSWER = 'Прости, но я не понимаю, что ты имеешь ввиду 😔'
