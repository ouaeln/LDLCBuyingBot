from telethon.sync import TelegramClient
import configparser
import selenium
import re

def SelectGPU(GPU):
    if GPU == '3060 Ti':
        PriceOfGPU = '419'
        return PriceOfGPU
    elif GPU == '3070':
        PriceOfGPU = '519'
        return PriceOfGPU
    elif GPU == '3070 Ti':
        PriceOfGPU = '619'
        return PriceOfGPU
    elif GPU == '3080':
        PriceOfGPU = '719'
        return PriceOfGPU
    elif GPU == '3080 Ti':
        PriceOfGPU = '1,199'
        return PriceOfGPU


def TelegramMonitor(PriceOfGPU):
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
        for message in client.iter_messages(chat, limit=1, search='(FR)** 💰 €'+PriceOfGPU+'.00'):
            MessageDictionary = str(message.to_dict().get('message'))
            MessageTimeStamp = message.date
            regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
            url = re.findall(regex, MessageDictionary)
            url = str(url).strip('[()]').replace("'", '').replace(",", '').replace(' ', '')
            return url, MessageTimeStamp

