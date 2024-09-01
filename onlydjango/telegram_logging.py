import logging
import os

import requests
from dotenv import load_dotenv


class TelegramBotHandler(logging.Handler):
    def __init__(self, telegram_bot_token, telegram_chat_id):
        logging.Handler.__init__(self)
        self.telegram_bot_token = telegram_bot_token
        self.telegram_chat_id = telegram_chat_id
        self.telegram_base_url = f"https://api.telegram.org/bot{self.telegram_bot_token}/"

    def sendMessage(self, message):
        res = requests.get(
           self.telegram_base_url + f"sendMessage?chat_id={self.telegram_chat_id}"
                                    f"&text=```ServerError {message}```"
                                    f"&parse_mode=MarkdownV2"
        )
        print(res.text)
        print(self.telegram_bot_token)

    def emit(self, record):
        log_entry = self.format(record)
        self.sendMessage(log_entry)



# test log
if __name__ == "__main__":
    load_dotenv(override=True)
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    print(bot_token)

    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    print(chat_id)



    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(
        TelegramBotHandler(
            os.getenv("TELEGRAM_BOT_TOKEN"), os.getenv("TELEGRAM_CHAT_ID")
        )
    )
    logger.error("test error log")
