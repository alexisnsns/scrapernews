import requests
from bs4 import BeautifulSoup

def scrape():
    url = "https://www.newyorker.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    results = soup.find_all(class_="summary-item__hed-link")
    links, titles, descs = [], [], []

    for div in results[:10]:
        if div:
            href = 'https://www.newyorker.com' + div.get('href')
            text = div.get_text(strip=True)
            links.append(href)
            titles.append(text)

    # optional: fetch short description
    for link in links:
        try:
            article_page = requests.get(link)
            article_soup = BeautifulSoup(article_page.content, 'html.parser')
            description_divs = article_soup.find_all(class_=["ContentHeaderDek-bIqFFZ", "SplitScreenContentHeaderDek-emptdL"])
            if description_divs:
                descs.append(description_divs[0].get_text(strip=True))
            else:
                descs.append('-')
        except Exception:
            descs.append('-')

    return titles, descs, links
