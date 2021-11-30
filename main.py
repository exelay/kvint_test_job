from loguru import logger

from core.telegram_bot import bot

if __name__ == '__main__':
    logger.info('Telegram bot started')
    bot.infinity_polling()
