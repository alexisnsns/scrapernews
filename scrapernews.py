import requests
from bs4 import BeautifulSoup

print("Let's scrap the news")


URL = "https://www.lemonde.fr/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")


results = soup.find_all(class_="article__title")

for i, result in enumerate(results[:5]):
    print(f"Result {i + 1}: {result.get_text()}")
