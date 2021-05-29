# import the library to query a website
import requests

from bs4 import BeautifulSoup

# Specify a  URL
wiki_link = "https://en.wikipedia.org/wiki/List_of_Asian_countries_by_population"
link = requests.get(wiki_link).text
soup = BeautifulSoup(link, 'html.parser')
# print(soup.prettify())

the_table = soup.find('table', class_="sortable wikitable")
all_links = the_table.find_all("a")

# print(all_links)
countries = []
for link in all_links:
    if link.get('title') is not None:
        countries.append(link.get('title'))

print(countries)
