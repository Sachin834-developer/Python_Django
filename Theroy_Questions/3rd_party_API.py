"""
integrating third-party APIs with Python is a common task, and it usually involves sending HTTP requests
 to the API and handling the responses. One of the most popular libraries for making HTTP requests in
 Python is requests.
"""

import requests

BASE_URL = "https://api.restful-api.dev/objects"
API_KEY = "api_key_here"

params = {"appid": API_KEY, "city": "Blore"}
print("outside try")
try:
    print("inside try")
    response = requests.get(BASE_URL)  # params=params
    print(f"{response=}")

    # Raise an exception for HTTP errors
    response.raise_for_status()

    # Parse the JSON response
    object_data = response.json()

    print(f"{object_data=}")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP Erro occured: {http_err}")
except Exception as error:
    f"Unknown Error: {error}"
