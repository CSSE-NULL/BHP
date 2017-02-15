import urllib2

url = "http://www.360.cn/"

headers = {}
headers['User-Agent'] = "Googlebot"

request = urllib2.Request(url,headers=headers)
response = urllib2.urlopen(request)

print response.read().decode("utf-8")
response.close()