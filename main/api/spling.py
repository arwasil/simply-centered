import requests, simplejson as json

def recommendations(category):
    params = {
        'limit': 8,
        'format': 'json',
        'tags': [category]
    }

    url = 'http://7gportal.spling.com/api/2/recommendation/'
    response = requests.get(url, params=params)
    try:
        spling_data = response.json()['items']
    except:
        spling_data = []

    return spling_data