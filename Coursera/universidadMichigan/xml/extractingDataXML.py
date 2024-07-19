import urllib.request
import xml.etree.ElementTree as ET

sumTotal = 0

url = 'http://py4e-data.dr-chuck.net/comments_2055742.xml'
uh = urllib.request.urlopen(url)
data = uh.read()
tree = ET.fromstring(data)
comments = tree.findall('comments/')

for item in comments:
    sumTotal += int(item.find('count').text)

print(sumTotal)