#!/usr/bin/python

#protocol: http, https, ftp
#host: url
#port: port number http = 80, https = 443
#path: path to desired webpage
#querystring: key value pair with &
#fragment: last section of desired webpage

from urllib import request
from urllib import parse

#request: opens urls
#response: internal parsing
#error: request exceptions
#parse: useful url function

#print(dir(urllib))
#print(dir(request))
resp = request.urlopen('https://www.wikipedia.org')
print(type(resp))
if resp.code == 200:
    print('200 -Okay - Good response, length in bytes: {}'.format(resp.length))
else:
    print('{} - return code'.format(resp.code))

print(resp.peek())
data = resp.read()
html = data.decode()

#https://www.youtube.com/watch?v=uXo3nZIpSNU

v_id = {'v':'uXo3nZIpSNU'}
query_string = parse.urlencode(v_id)
url = 'https://www.youtube.com/watch?' + query_string
resp = request.urlopen(url)
if resp.code == 200:
    video_info = resp.read().decode()
    print(video_info[:500])
#print(video_info)

