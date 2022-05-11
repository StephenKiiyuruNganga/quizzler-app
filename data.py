import requests

questions_api = "https://opentdb.com/api.php"
questions_api_params = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get(url=questions_api, params=questions_api_params)
response.raise_for_status()
data = response.json()
question_data = data["results"]
