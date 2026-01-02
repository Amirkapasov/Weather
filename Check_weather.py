import requests
from bs4 import BeautifulSoup

def get_weather(city):
    link = f"https://tengrinews.kz/weather/{city}/day/"
    response = requests.get(link).text
    soup = BeautifulSoup(response, "lxml")
    block = soup.find("div",class_="weather-city-all")

    gradus = block.find("p",class_="weather-city-all-temp-value")
    pred_gradus = block.find("p",class_="weather-city-all-temp-desc")

    date = block.find("date",class_="weather-city-day")

    return "\nTemp: "+gradus.text.strip()+'\n'+ pred_gradus.text.strip()+'\n'+"Today date: "+date.text.strip()
