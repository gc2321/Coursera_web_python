import urllib, json

#url = "http://python-data.dr-chuck.net/comments_42.json"
url = "http://python-data.dr-chuck.net/comments_258488.json"

response = urllib.urlopen(url)
data = json.loads(response.read())

comments = data['comments']

sum = 0

for each in comments:
    sum += each['count']

print sum

