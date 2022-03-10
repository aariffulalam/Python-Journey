# print('i am "beautiful soup".')

#Beautiful Soup is a Python package for parsing HTML and XML documents (including having malformed markup,
# i.e. non-closed tags, so named after tag soup). It creates a parse tree for 
# parsed pages that can be used to extract data from HTML, whi#!/usr/bin/env python3


# Syntext:-
# Anchor extraction from HTML document
# from bs4 import BeautifulSoup
# from urllib.request import urlopen
# with urlopen('https://en.wikipedia.org/wiki/Main_Page') as response:
#     soup = BeautifulSoup(response, 'html.parser')
#     for anchor in soup.find_all('a'):
#         print(anchor.get('href', '/'))


#  when we "scrap" the data, we got data in form of "HTML". so to collect the data in the sutable 
# form like "xml/JSON" we have use this "beautiful soup" packeg of "python".

import json
import requests
from bs4 import BeautifulSoup

url = requests.get("http://saral.navgurukul.org/api/courses").text
soup=BeautifulSoup(url,"html.parser")
with open("api_soup.json","w") as obj:
    json.dump(soup.json(),obj,indent=10)
with open("api.json","r") as b:
    d=json.load(b)
e=json.loads(d)
print(type(e))


