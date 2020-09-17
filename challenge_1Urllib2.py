import json
import urllib2
url = "https://api.github.com/repos/actions/runner/releases/latest"
response = urllib2.urlopen(url)
data = response.read()
values = json.loads(str(data))
print (values)['tag_name']
x = (values)['assets'][0]
#print (len(values))
#print (len(x))
#print (type(x))
print (x)['browser_download_url']
#y = (x.items())
#print (y)
