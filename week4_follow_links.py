import urllib
from bs4 import BeautifulSoup


def visit(url):
    """
    visit url and return soup('a')
    :param url: url
    :return: soup('a')
    """
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")
    return soup('a')

#url = 'http://python-data.dr-chuck.net/known_by_Fikret.html'
url = 'http://python-data.dr-chuck.net/known_by_Greer.html'

result= []
position = 18
times = 7

for i in range(times):
    tags = visit(url)
    for idx in range(len(tags)):
        if idx == position-1:
            result.append(str(tags[idx].contents[0]))
            url = tags[idx].get('href', None)

#print result
print result[-1]