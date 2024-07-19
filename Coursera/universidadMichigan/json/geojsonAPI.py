import urllib.request, urllib.parse
import json, ssl

serviceURL = 'https://py4e-data.dr-chuck.net/opengeo?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
address = address.strip()
parms = dict()
parms['q'] = address

url = serviceURL + urllib.parse.urlencode(parms)

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
js = json.loads(data)

plus_code = js['features'][0]['properties']['plus_code']

print(plus_code)