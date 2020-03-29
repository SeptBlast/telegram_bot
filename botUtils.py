import requests
import json

def get_url_response(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

def get_json_from_url(url):
    content = get_url_response(url)
    contentJson = json.loads(content)
    return contentJson

def send_message(URL, text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url_response(url)


