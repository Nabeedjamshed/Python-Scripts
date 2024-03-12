# import requests

# api = "https://newsapi.org/v2/everything?q=tesla&from=2024-01-25&sortBy=publishedAt&apiKey=efccc6bc0cdd4830be9f718db8660cc3"

# json_data = requests.get(api).json()
# print(json_data)

import requests

api_key = 'efccc6bc0cdd4830be9f718db8660cc3'
url = 'https://newsapi.org/v2/top-headlines'
parameters = {
    'apiKey': api_key,
    'country': 'us',  # Specify country (optional)
}

response = requests.get(url, params=parameters)
data = response.json()

if data['status'] == 'ok':
    headlines = data['articles']
    for headline in headlines:
        print(headline['title'])
else:
    print("Error fetching headlines:", data['message'])
