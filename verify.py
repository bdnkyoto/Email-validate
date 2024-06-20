import requests
import json

email = "batsinyakotyo@gmail.com"
api_key = "13e421cfb09d47cc995f2cb6ce7470b5"
url = f"https://emailvalidation.abstractapi.com/v1/?api_key={api_key}&email={email}"

try:
    response = requests.get(url)
    response.raise_for_status()  #if the request was unsuccessful
    data = response.json()  # Parse the json response

    print("Status Code:", response.status_code)
    print("Response:", json.dumps(data, indent=4))  # format the JSON response

except requests.exceptions.RequestException as e:
    print("Error:", e)
