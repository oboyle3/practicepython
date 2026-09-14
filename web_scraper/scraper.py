#Make a request to a webpage and print the webpage's HTML.
import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.scrapethissite.com/pages/forms/")
soup = BeautifulSoup(response.text, "html.parser")
# print(response.text)
# soup.print("title")
print(soup.find("title"))
print("-------------------")
print(soup.find("title").text)