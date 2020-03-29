import json
import datetime
import botUtils

BASE_URL = "https://covidapi.info/api/v1"
LATEST_DATE = "/latest-date"
LATEST = "/latest"
COUNTRY = "/country/"

def get_count_for_country(countryName):
    if (countryName == "global"):
        url = BASE_URL + "/" + countryName + LATEST
    else:
        # https://covidapi.info/api/v1/country/IND/latest
        url = BASE_URL + COUNTRY + countryName + LATEST
    
    # response = botUtils.get_url_response(url)
    return url

def generate_covid_message(countryName):
    latest = botUtils.get_url_response(BASE_URL + LATEST_DATE)
    jsonData = botUtils.get_json_from_url(get_count_for_country(countryName))
    stringMessage = "COVID-19 Demograph till date {} of Country {}: \n \t Total Positive Cases : {} \n \t Total Recovery Count : {} \n \t Total Deaths : {}".format(latest, countryName, jsonData["result"][latest]["confirmed"], jsonData["result"][latest]["recovered"], jsonData["result"][latest]["deaths"])
    return stringMessage


print (generate_covid_message("IND"))
