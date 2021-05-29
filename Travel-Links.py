import requests
from bs4 import BeautifulSoup

import re

link = "http://www.dr-chuck.com/page1.htm"
link = requests.get(link).text

soup = BeautifulSoup(link, "html.parser")
print(soup)

reference = soup.find('a')
reference_link = reference.get('href')
reference_link = requests.get(reference_link).text
print("************Second Page***************")

soup = BeautifulSoup(reference_link, "html.parser")
print(soup)