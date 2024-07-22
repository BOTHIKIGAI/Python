import sqlite3
import re

fhand = open(r'..\..\..\..\assets\plaintxt\mbox.txt')
conn = sqlite3.connect('DB2.sqlite')
cur = conn.cursor()

domainMailCount = dict()

for line in fhand:
    if not line.startswith('From: '): continue
    domainMail = re.findall(r'@([^ ]*)', line)[0][0:-1]

    if not domainMailCount.get(domainMail):
        domainMailCount[domainMail] = 1
    else:
        domainMailCount[domainMail] = domainMailCount[domainMail] + 1

for key, value in domainMailCount.items():
    cur.execute(''' INSERT INTO Counts (org, count) VALUES (?, ?) ''', (key, value,))

conn.commit()