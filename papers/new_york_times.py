import requests
from bs4 import BeautifulSoup

def scrape():
    url = "https://www.nytimes.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    results = soup.find_all(class_="css-9mylee")
    titles, links = [], []

    for div in results[:10]:
        nested_div = div.find(class_="css-xdandi")
        if nested_div:
            text = nested_div.get_text(strip=True)
            href = div.get('href')
            if text and href:
                links.append(href)
                titles.append(text)

    descs = ["-" for _ in titles]
    return titles, descs, links
