import datetime
import requests

APP_ID = "5caa9c56"
APP_KEY = "61c58b0b6c433b588c261bc3bf381eb9"

query = input("Enter query ")

API_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

query_parameter = {
    "query": query
}

request = requests.post(url=API_endpoint, json=query_parameter, headers=headers)

data_list = request.json()["exercises"]

sheety_API_endpoint = "https://api.sheety.co/16276d59486a8c0fd7fc97afa9e6760a/workout/workouts"

for data in data_list:
    duration = data['duration_min']
    name = str(data["name"]).title()
    calories = data["nf_calories"]
    date = datetime.datetime.now().strftime("%d/%m/%Y")
    time = datetime.datetime.now().strftime("%H:%M:%S")
    parameters = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": name,
            "duration": duration,
            "calories": calories
        }
    }
    response = requests.post(sheety_API_endpoint, json=parameters)
    print(response.json())
