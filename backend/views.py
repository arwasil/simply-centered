from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

import requests
from requests.auth import HTTPBasicAuth
import simplejson as json
import urllib, urllib2, base64

from main.models import *

def authorization():
    url = 'https://simplycentered.trap.it/api/v2/sc/auth/basic/verify/'
    headers = {'Content-Type': 'application/json'}
    request_data = settings.TRAP_IT_ACCESS_INFO

    response = requests.post(url, data=json.dumps(request_data), headers=headers)
    data = response.json()
    auth = HTTPBasicAuth(data['user_id'], data['session'])
    return auth

def list(request):
    auth = authorization()

    url = 'https://simplycentered.trap.it/api/v3/sc/trapdumps/bundles/'
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}

    response = requests.get(url, auth=auth, headers=headers)
    return render(request, 'backend/list.html', {"list": response.json()})

def bundle(request, id):
    auth = authorization()

    url = 'https://simplycentered.trap.it/api/v3/sc/traps/%s/queue/?expand_doc_sources_and_origins=true&invisible_only=true&with_origin_owner=true&size=20&page=0&pretty=true' % id
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}

    response = requests.get(url, auth=auth, headers=headers)
    data = response.json()
    #print json.dumps(data['records'][0], indent=4*' ')

    return render(request, 'backend/bundle.html', {"list": data['records']})

def add_to_spling(request):
    link = request.POST.get('link')
    image = request.POST.get('image')
    title = request.POST.get('title')
    genre = request.POST.get('genre').lower()
    
    access = settings.SPLING_COM_ACCESS_INFO

    data = {'Link': link,
            'Title': title, 
            'ImageURL': image,
            'Genre': genre in SPLING_CATEGORIES and SPLING_CATEGORIES[genre] or ''}

    create_url = '%s/spling/' % access['url']
    data = json.dumps(data)
    auth = HTTPBasicAuth(access['username'], access['password'])
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    resp = requests.post(create_url, data=data, auth=auth, headers=headers)

    if resp.status_code == 200:
        return HttpResponse('success')
    else:
        return HttpResponse(resp.json()['detail'])
