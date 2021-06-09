# With an use of Weather API ,country-converter 0.7.3 I've build an app to show current weather in
# specific city entered by input.
import requests
import country_converter as coco
from pprint import pprint


api_key = '197114120126a5a6ed2aa93ee517a5ae'

# function to search weather forecast by city name with api openweathermap


def forecast(city_name):
    url = 'http://api.openweathermap.org/data/2.5/weather?' + \
        "appid=" + api_key + "&q=" + city_name
    response = requests.get(url)
    x = response.json()
    return x


def check_weather():
    city_name = input("Enter city name : ")
    result = forecast(city_name)
    converter = coco.CountryConverter()

    if result["cod"] != "404":
        # search for temperature( which is converted from original Kevin into Celcius), humidity and  atmosphericpressure
        y = result["main"]
        current_temperature_kev = y["temp"]
        current_temperature_c = int(current_temperature_kev - 273.15)
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]

    # use package country converter to convert iso country code ex. UA into official name of the country
        iso3_codes = result['sys']
        country = iso3_codes['country']
        country_official_name = converter.convert(
            names=country, to='name_official')
# show type of the weather
        z = result["weather"]
        weather_description = z[0]["description"]

        print(f"Current temperature in {city_name}(in {country_official_name}) is {current_temperature_c}°C,\n the atmospheric pressure is {current_pressure} hPa,\n humidity {current_humidity} % and\n there are(is): {weather_description}.")

    else:
        print(f"Sorry but we didn't found {city_name} as a city name.")


check_weather()
