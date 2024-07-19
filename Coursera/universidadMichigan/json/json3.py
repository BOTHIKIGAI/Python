import urllib.request, urllib.parse
import json, ssl

serviceUrl = 'http://py4e-data.dr-chuck.net/comments_2055743.json'
count = 0;

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

uh = urllib.request.urlopen(serviceUrl, context=ctx)
data = uh.read()

info = json.loads(data)

for x in range (len(info['comments'])):
    count += (info['comments'][x]['count'])

print(count);