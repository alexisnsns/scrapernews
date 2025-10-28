import requests
from bs4 import BeautifulSoup

def scrape():
    url = "https://www.ft.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    ftresults = soup.find_all(class_="js-teaser-headline")
    ft_links, ft_titles = [], []

    for div in ftresults[:10]:
        anchor = div.find('a')
        if anchor:
            href = 'https://www.ft.com' + anchor.get('href')
            text = anchor.get_text(strip=True)
            if href and text:
                ft_links.append(href)
                ft_titles.append(text)

    descs = ["-" for _ in ft_titles]
    return ft_titles, descs, ft_links
