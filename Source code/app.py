import requests
from bs4 import BeautifulSoup
request = requests.get("https://www.johnlewis.com/house-by-john-lewis-nova-fabric-office-chair/p3082162")
content = request.content
soup = BeautifulSoup(content,"html.parser")
element = soup.find("img")
# <p class="u-centred price">£70.00
print(element.txt)                                                    # this fucking code returning NONE value fuckkkkkkkkkkkk.......it should return price of eliment..
