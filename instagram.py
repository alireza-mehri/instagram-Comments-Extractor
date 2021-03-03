from bs4 import BeautifulSoup
import urllib.parse
from urllib.request import urlopen

# parsing getcombot url  
# get url
html_page = urlopen("your getcombot.com Url")

soup = BeautifulSoup(html_page, 'html.parser')
# find table with "main" id in html page
infoBarTag = soup.find('table', id="main")

#if your tables or elemets have a children
for child in infoBarTag.children:
    temp = child.findAll('td', align="left")[1]
    print(temp.get_text())
