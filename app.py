import requests

user_api = "17493c079e28c41ec54beae628666f00"

city_name = input("Enter city name: ")

request_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + \
    city_name+"&appid="+user_api

api_link = requests.get(request_api_link)

data = api_link.json()  # Transfer the data in json format

# if Data["cod"] == "404" or Data["cod"] == "401" or Data["cod"] == "429" or Data["cod"] == "500" or Data["cod"] == "502" or Data["cod"] == "503" or Data["cod"] == "504":
#     print("Data Not Found")
# else:
#     # print(Data)
#     Weather_Curr_City = Data["weather"][0]["main"]
#     print(f"Current weather is {Weather_Curr_City}.")
try:
    weather_curr_city = data["weather"][0]["main"]
    print(f"Current weather is {weather_curr_city}.")
except:
    print("Data Not Found")
