import urllib.request
import json
import codecs

websiteURL = "http://macvendors.co/api/"
macAddress = "44-39-C4-55-67-FE"

requestInfo = urllib.request.Request(websiteURL + macAddress,  headers={'User-Agent' : "API Browser"})
macRequest = urllib.request.urlopen(requestInfo)
jsonData = json.load(macRequest)

print(jsonData['result']['company'] + ", " + jsonData['result']['address'])
