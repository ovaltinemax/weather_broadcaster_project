import requests
import json

def Wind(weather_data): #風速
    wdir = weather_data["records"]["location"][0]["weatherElement"][1]
    wdsd = weather_data["records"]["location"][0]["weatherElement"][2]
    return {wdsd["elementName"] : str(wdsd["elementValue"])+" m/s" , wdir["elementName"] : str(wdir["elementValue"])+" 度"}



def Temp(weather_data): #溫度
    temp = weather_data["records"]["location"][0]["weatherElement"][3]
    d_tx = weather_data["records"]["location"][0]["weatherElement"][10]
    d_tn = weather_data["records"]["location"][0]["weatherElement"][12]
    return {d_tx["elementName"] : str(d_tx["elementValue"])+"°" ,temp["elementName"] : str(temp["elementValue"])+"°" , d_tn["elementName"] : str(d_tn["elementValue"])+"°"}


def Humd(weather_data): #濕度
    humd = weather_data["records"]["location"][0]["weatherElement"][4]
    return str((float(humd["elementValue"])*100))+"%"


def Weather_status(weather_data):  #天氣狀況
    status = weather_data["records"]["location"][0]["weatherElement"][14]
    return str(status["elementValue"])+"天"


def WeatherWrapper(weather_api_key,locationName):
    weatherURL="https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0001-001"
    params = {
    "Authorization":weather_api_key,
    "locationName": locationName
    }
    response = requests.get(weatherURL, params=params)
    return response
    




def get_json_content(path):
    with open(path , "r", encoding="utf-8") as js:
        content = json.load(js)
        js.close()
    return content

