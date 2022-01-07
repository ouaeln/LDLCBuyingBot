import configparser
from telethon.sync import TelegramClient

config = configparser.ConfigParser()
config.read("config.ini")

# Setting configuration values
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
api_hash = str(api_hash)
phone = config['Telegram']['phone']
username = config['Telegram']['username']

chat = 'https://t.me/joinchat/AAAAAEii3xT81U1A6tLjrQ'

with TelegramClient(username, api_id, api_hash) as client:
    for message in client.iter_messages(chat, limit = 100, search= '(FR)** 💰 €519.00'):
        print(message.date, ':', message.text)
