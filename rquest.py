# import requests
# response = requests.get("https://www.google.com")
# print(response.text)

import requests 
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"
r = requests.get(url)
# print(r.text)


soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
for heading in soup.find_all("h2"):
  print(heading.text)

# There is another module called BeautifulSoup which is used for web scraping(extract data from web pages) in Python. I have personally used bs4 module to finish a lot of freelancing task.