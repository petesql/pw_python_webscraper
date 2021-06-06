import requests 
from bs4 import BeautifulSoup

page = requests.get("https://peter-whyte.com")
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.get_text())