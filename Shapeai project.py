import requests
# import os
from datetime import datetime

api_key = 'f60e643b831ae1f92572268c11b00a00'

location = input("Enter the city name :\n ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" +'pune'+ "&appid=" + 'f60e643b831ae1f92572268c11b00a00'
api_link = requests.get(complete_api_link)
api_data = api_link.json()

# Alloting the required variable created to store the data ....

temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print("*************************************************************\n")

print("Weather Status for - {}  || {}".format(location.upper(), date_time))

print("\n**************************************************************\n")

print("Current temperature : {:.2f} deg C".format(temp_city))
print("Current weather description  :", weather_desc)
print("Current Humidity      :", hmdt, '%')
print("Current wind speed    :", wind_spd, 'kmph')

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

# list for making the info converted to text format.

txtlist = [temp_city, weather_desc, hmdt, wind_spd, date_time]

# using open() buit-in function to write to a text file

with open("textfile.txt", mode='w', encoding='utf-8') as f:
    # encoding = utf-8 for linux and cp1252 for win
    f.write("**************************************************************** \n ")

    f.write("Weather Status for - {}  || {}".format(location.upper(), date_time))

    f.write("\n ************************************************************** \n")
    f.write("Current temperature : {:.2f} deg C\n".format(txtlist[0]))

    f.write("{},{} \n".format("Current weather description  :", txtlist[1]))
    f.write("{},{},{} \n".format("Current Humidity      :", txtlist[2], "%"))
    f.write("{},{},{} \n".format("Current wind speed    :", txtlist[3], "kmph"))

    f.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")