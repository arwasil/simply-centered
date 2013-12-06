import requests, simplejson as json

def recommendations(category, area):
    limit = 8
    limit = limit - min(category.sub_categories(area).count(), 4)
    limit = limit - min(category.promotion_set.count(), 4)

    spling_data = []

    if limit > 0:
        params = {
            'limit': limit,
            'format': 'json',
            'tags': [category.name]
        }

        url = 'http://7gportal.spling.com/api/2/recommendation/'
        response = requests.get(url, params=params)
        try:
            spling_data = response.json()['items']
        except:
            pass

    return spling_data