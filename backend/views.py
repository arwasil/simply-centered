from django.shortcuts import render
import urllib, urllib2, simplejson, base64

def authorization():
    request_data = {
        "auth_id":"bmcfarland@spling.com",
        "auth_secret":"Discover"
    }
    req = urllib2.Request(
      'https://simplycentered.trap.it/api/v2/sc/auth/basic/verify/',
      data=simplejson.dumps(request_data),
      headers={
          "Content-Type": "application/json",
      })
    response = urllib2.urlopen(req)
    data = simplejson.load(response)
    return data

def list(request):
    auth = authorization()

    url = 'https://simplycentered.trap.it/api/v3/sc/search/?pretty=true'
    req = urllib2.Request(url)
    base64string = base64.encodestring('%s:%s' % (auth['user_id'], auth['session'])).replace('\n', '')
    req.add_header("Authorization", "Basic %s" % base64string)   

    values = {"query":"curated:true type:bundle ","order":"title","reverse":False,"language":"en","limit":50,"offset":0}
    data = urllib.urlencode(values)

    response = urllib2.urlopen(req, data)
    data = simplejson.load(response)

    return render(request, 'backend/list.html', {"list": data})

def bundle(request, id):
    auth = authorization()

    url = 'https://simplycentered.trap.it/api/v3/sc/traps/%s/queue/?expand_doc_sources_and_origins=true&invisible_only=true&with_origin_owner=true&size=20&page=0&pretty=true' % id
    req = urllib2.Request(url)
    base64string = base64.encodestring('%s:%s' % (auth['user_id'], auth['session'])).replace('\n', '')
    req.add_header("Authorization", "Basic %s" % base64string)   
    response = urllib2.urlopen(req)
    data = simplejson.load(response)

    return render(request, 'backend/bundle.html', {"list": data['records']})
