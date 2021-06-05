import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.salahtimes.com/bangladesh/narayanganj')
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.find(id="prayerContainer"))
