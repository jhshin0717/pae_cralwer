import requests
from bs4 import BeautifulSoup


req = requests.get('https://beomi.github.io/')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
