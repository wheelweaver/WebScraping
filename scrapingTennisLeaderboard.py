import requests
from bs4 import BeautifulSoup

#get the data
data = requests.get('https://www.atptour.com/en/rankings/singles')
print(data)
