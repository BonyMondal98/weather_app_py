import requests

user_API = "17493c079e28c41ec54beae628666f00"

City_Name = input("Enter city name: ")

Request_API_Link = "https://api.openweathermap.org/data/2.5/weather?q=" + \
    City_Name+"&appid="+user_API

API_Link = requests.get(Request_API_Link)

Data = API_Link.json()  # Transfer the data in json format

# if Data["cod"] == "404" or Data["cod"] == "401" or Data["cod"] == "429" or Data["cod"] == "500" or Data["cod"] == "502" or Data["cod"] == "503" or Data["cod"] == "504":
#     print("Data Not Found")
# else:
#     # print(Data)
#     Weather_Curr_City = Data["weather"][0]["main"]
#     print(f"Current weather is {Weather_Curr_City}.")
try:
    Weather_Curr_City = Data["weather"][0]["main"]
    print(f"Current weather is {Weather_Curr_City}.")
except:
    print("Data Not Found")
