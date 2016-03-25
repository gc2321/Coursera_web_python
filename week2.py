import urllib2
import re

#url = 'http://python-data.dr-chuck.net/regex_sum_42.txt'
url = 'http://python-data.dr-chuck.net/regex_sum_258482.txt'
netfile = urllib2.urlopen(url)
data = netfile.read()
result = sum(map(int, re.findall('[0-9]+', data)))

print result

