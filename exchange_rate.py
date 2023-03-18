import requests

# Where USD is the base currency you want to use
url = 'https://v6.exchangerate-api.com/v6/a1adfd4fbb31605d813e708c/pair/USD/UZS'

# Making our request
response = requests.get(url)
data = response.json()

# Your JSON object
print(data["conversion_rate"])