from loguru import logger

from telegram_bot import bot

if __name__ == '__main__':
    logger.info('Telegram bot started')
    bot.infinity_polling()
