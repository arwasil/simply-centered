import requests, simplejson as json

def recommendations(category, area, spec_limit=None):
    limit = 8
    limit = limit - min(category.sub_categories(area).count(), 4)
    if category.skyscraper_mode:
        limit = limit - 2 - min(category.promotion_set.count(), 2)
    else:
        limit = limit - min(category.promotion_set.count(), 4)
    if spec_limit:
        limit = spec_limit

    spling_data = []

    if limit > 0:
        params = {
            'limit': limit,
            'format': 'json',
            'tags': [category.name],
            'thumbnails[]': ['300x300', '140x300', '140x620']
        }

        url = 'http://7gportal.spling.com/api/2/recommendation/'
        response = requests.get(url, params=params)
        try:
            spling_data = response.json()['items']
        except:
            pass

        
        for data in spling_data:
            # fix link for youtube items
            if data['EmbedlyType'] in [0, 1, 2]:
                data['Link'] = data['Link'].replace('watch?v=', 'embed/').replace('&feature=', '?feature=')
            
            data['type'] = data['MediaType']['name']
            data['lightbox'] = data['type'] in ['Video', 'Picture']


    return spling_data