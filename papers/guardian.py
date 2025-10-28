import requests
from bs4 import BeautifulSoup

def scrape():
    url = "https://www.theguardian.com/international"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    tg_results = soup.find_all("a", attrs={"aria-label": True, "href": True})
    tg_links, tg_titles = [], []

    for a_tag in tg_results:
        href = a_tag.get("href")
        title = a_tag.get("aria-label")

        if href and title and href.startswith("/"):
            full_url = "https://www.theguardian.com" + href
            tg_links.append(full_url)
            tg_titles.append(title)

    seen = set()
    unique = [(t, l) for t, l in zip(tg_titles, tg_links) if not (l in seen or seen.add(l))]
    tg_titles, tg_links = zip(*unique[:10]) if unique else ([], [])

    descs = ["-" for _ in tg_titles]
    return tg_titles, descs, tg_links
