import requests
from bs4 import BeautifulSoup

def scrape():
    url = "https://www.economist.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    results = soup.find_all(class_="ekfon2k0")
    titles, links = [], []

    for div in results[:10]:
        anchor = div.find('a')
        if anchor:
            href = 'https://www.economist.com' + anchor.get('href')
            text = anchor.get_text(strip=True)
            if href and text:
                links.append(href)
                titles.append(text)

    descs = ["-" for _ in titles]
    return titles, descs, links
