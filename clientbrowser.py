import urllib.request

def reqUrl(data) :
    websiteurl = urllib.request.urlopen(data)
    rawData = websiteurl.read()
    statusCode = websiteurl.getcode()
    header = websiteurl.getheaders()
    server = websiteurl.info()
    print('HTML Data:  \n', rawData)
    print ('-'*80)
    print('Status Code: ', statusCode)
    print ('-'*80)
    print('Header Information: \n', header)
    print ('-'*80)
    print('Server Information: \n', server)
    print ('-'*80)

    f = open('websiteHTML.html', 'wb')
    f.write(rawData)
    f.close()
    print('HTML saved to websiteHTML.html')

reqUrl(input('What website to scan?: '))
