# This program was created for an assignment.  The objective of assignment was
# to use urllib and BeautifulSoup to scan a webpage for anchor tags, find a specific
# anchor tag, then to follow that anchor tag, rinse and repeat 7 times and the last
# url has a person's name associated with it, that is the answer to the problem.
# Below are the actual instructions for the problem.

# The program will use urllib to read the HTML from the data files below, extract the
# href= values from the anchor tags, scan for a tag that is in a particular position
# relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.
# Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
# Last name in sequence: Anayah
# Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Marla.html
# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
# Hint: The first character of the name of the last page that you will load is: E

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
ctr = 0
while ctr < 7:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    sn = list()
    for tag in tags[17:18]:
        sn = tag.get('href', None)
        nurl = sn
        url = nurl
        ctr = ctr + 1
        print(nurl)
