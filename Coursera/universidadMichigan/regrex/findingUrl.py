import re

x = '<p>Please click <a href="http://www.dr-chuck.com">here</a></p>';
print(re.findall('href="(.+)"', x))