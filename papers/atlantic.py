# papers/atlantic.py
import requests
from bs4 import BeautifulSoup

def scrape():
    url = "https://www.theatlantic.com/"
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")

    titles, descs, links = [], [], []

    # Find top stack articles
    articles = soup.find_all("article", class_="SmallPromoItem_root__nkm_2")

    for article in articles[:10]:
        # Title & link
        h2 = article.find("h2", class_="SmallPromoItem_title__0zOZ0")
        a_tag = h2.find("a") if h2 else None
        title = a_tag.get_text(strip=True) if a_tag else "-"
        link = a_tag["href"] if a_tag else None

        # Description: The Atlantic doesn't always have a dedicated description
        desc = "-"  # fallback
        desc_div = article.find("p")
        if desc_div:
            desc = desc_div.get_text(strip=True)

        # Make sure the link is absolute
        if link and link.startswith("/"):
            link = "https://www.theatlantic.com" + link

        titles.append(title)
        descs.append(desc)
        links.append(link)

    return titles[:10], descs[:10], links[:10]

# Example usage
if __name__ == "__main__":
    titles, descs, links = scrape()
    for t, d, l in zip(titles, descs, links):
        print(t)
        print(d)
        print(l)
        print("-"*80)
