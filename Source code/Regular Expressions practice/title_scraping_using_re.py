

                            # little web title scraping with little regex


import re,urllib
import urllib.request

sites = ['http://google.com','https://www.facebook.com/','https://www.amazon.com/','https://www.udacity.com/']

for t in sites:
    print('Searching.....')
    u = urllib.request.urlopen(t)
    text = u.read()
    title = re.findall('<title>.*</title>',str(text),re.IGNORECASE)
    print(title)
