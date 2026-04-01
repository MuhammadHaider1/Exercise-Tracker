import requests
from datetime import datetime
import os

#ADD YOUR PERSONAL DATA. USED BY THE EXERCISE & NUTRITION API TO CALCULATE CALORIES.
GENDER = "male"
WEIGHT_KG = 87.0
HEIGHT_CM = 180.34
AGE = 20


#NUTRITIONIX APP ID AND KEY.Actual values stored as environment variables.
APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]

exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
exercise_text = input("Tell me which exercise you did: ")



#NUTRITIONIX API CALL.
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

base_params = {
    "query": exercise_text,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
    "gender": GENDER
}

response = requests.post( url = exercise_endpoint , headers=headers, json=base_params)
result = response.json()
print(f"Nutritionix API call: \n {result} \n")

'''DATE TIME'''
today = datetime.now().strftime('%Y/%m/%d')
now_time = datetime.now().strftime('%X')


#SHEETY PROJECT API.CHECK YOUR GOOGLE SHEET NAME AND SHEETY ENDPOINT.
GOOGLE_SHEET_NAME = "workout"
sheety_endpoints = os.environ["SHEETY_ENDPOINT"]


#SHEETY PROJECT API CALL AND AUTHENTICATION.
for exercise in result["exercises"]:
    sheet_inputs = {
    "workout": {
        "date" : today,
        "time" : now_time,
        "exercise" : exercise["name"].title(),
        "duration" : exercise["duration_min"],
        "calories" : exercise["nf_calories"],

        }
    }

    # Sheety Authentication Option 2: Basic Auth
    sheet_response = requests.post(
        url=sheety_endpoints,
        json=sheet_inputs,
        auth=(
            os.environ["SHEETY_USERNAME"],
            os.environ["SHEETY_PASS"],
        )
    )

    print(f"Sheety Response: \n {sheet_response.text}")

