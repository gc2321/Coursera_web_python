import urllib
from bs4 import BeautifulSoup

#url = raw_input('Enter - ')			# allow enter webpage address
#url = 'http://python-data.dr-chuck.net/comments_42.html'
url = 'http://python-data.dr-chuck.net/comments_258487.html'

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "lxml")

tags = soup('span')

result =[]

for tag in tags:
    result.append(int (tag.contents[0] ))

print sum(result)