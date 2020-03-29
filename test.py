import requests
import json

latestDate = "https://covidapi.info/api/v1/latest-date"
latestDateUrl =  "https://covidapi.info/api/v1/country/IND/latest"

def get_url_response(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

def get_json_from_url(url):
    content = get_url_response(url)
    contentJson = json.loads(content)
    return contentJson

def generate_covid_message(countryName):
    latest = get_url_response(latestDate)
    jsonData = get_json_from_url(latestDateUrl)
    stringMessage = "COVID-19 Demograph till date {} of Country {}: \n \t Total Positive Cases : {} \n \t Total Recovery Count : {} \n \t Total Deaths : {}".format(latest, countryName, jsonData["result"][latest]["confirmed"], jsonData["result"][latest]["recovered"], jsonData["result"][latest]["deaths"])
    return stringMessage

print (generate_covid_message("India"))