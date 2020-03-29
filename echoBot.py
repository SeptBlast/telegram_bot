import json
import requests
import time
import botUtils
import covidRequest

TOKEN = "1069532617:AAFmJvWnTRgori-5FVEvaJ2mBXsDYyJ2ye8"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

def get_updates(offset=None):
    url = URL + "getUpdates"
    if offset:
        url += "?offset={}".format(offset)
    js = botUtils.get_json_from_url(url)
    return js

def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)

def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)

def echo_all(updates):
    for update in updates["result"]:
        try:
            # text = update["message"]["text"]
            text = covidRequest.generate_covid_message(update["message"]["text"])
            chat = update["message"]["chat"]["id"]
            botUtils.send_message(URL, text, chat)
        except Exception as e:
            print(e)

# def main():
#     last_textchat = (None, None)
#     while True:
#         text, chat = get_last_chat_id_and_text(get_updates())
#         if (text, chat) != last_textchat:
#             botUtils.send_message(URL, text, chat)
#             last_textchat = (text, chat)
#         time.sleep(0.5)

def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            echo_all(updates)
        time.sleep(0.5)


if __name__ == '__main__':
    main()