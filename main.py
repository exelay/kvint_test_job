from loguru import logger

from core.user_interfaces.telegram_bot import bot

if __name__ == '__main__':
    logger.info('Telegram bot started')
    bot.infinity_polling()
