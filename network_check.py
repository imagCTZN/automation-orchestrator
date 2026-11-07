import requests


try:
    response = requests.get('https://bing.com', timeout=5)
    print(response)
except requests.RequestException as e:
    print(e)