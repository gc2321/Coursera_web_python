import xml.etree.cElementTree as ET
import urllib
from xml.dom import minidom

#url = 'http://python-data.dr-chuck.net/comments_42.xml'
url = 'http://python-data.dr-chuck.net/comments_258484.xml'

usock = urllib.urlopen(url)
xmldoc = minidom.parse(usock)
usock.close()

# print as xml
#print xmldoc.toxml()

result =[]

# convert to string
data = ET.fromstring(xmldoc.toxml())
counts = data.findall('comments/comment/count')
for each in counts:
    result.append(int(each.text))

print sum(result)
