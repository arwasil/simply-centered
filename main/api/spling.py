import requests, simplejson as json

def get_spling_data(params):
    url = 'http://7gportal.spling.com/api/2/recommendation/'
    response = requests.get(url, params=params)

    try:
        spling_data = response.json()['items']
    except:
        spling_data = []
    
    for data in spling_data:
        data['type'] = data['MediaType']['name']

        # show lightbox for videos and pictures
        data['lightbox'] = data['type'] in ['Video', 'Picture']

        # fix link for youtube items
        if data['type'] == 'Video':
            data['Link'] = data['Link'].replace('watch?v=', 'embed/').replace('&feature=', '?feature=')

    return spling_data

def recommendations(category, area, spec_limit=None):
    limit = 8
    limit = limit - min(category.sub_categories(area).count(), 4)
    if category.skyscraper_mode:
        limit = limit - 2 - min(category.promotion_set.count(), 2)
    else:
        limit = limit - min(category.promotion_set.count(), 4)
    if spec_limit:
        limit = spec_limit

    if limit > 0:
        params = {
            'limit': limit,
            'format': 'json',
            'tags': [category.name],
            'thumbnails[]': ['300x300', '140x300', '140x620']
        }
        
        return get_spling_data(params)
    else:
        return []

def search(query):
    tags = query.split(' ')
    print query
    print tags
    params = {
        'format': 'json',
        'tags': tags
    }
    
    return get_spling_data(params)

