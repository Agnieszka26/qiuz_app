import requests
URL ='https://opentdb.com/api.php?amount=10&type=boolean'
response = requests.get(URL)
data = response.json()
question_data = data["results"]

