# papers/le_monde.py
import requests
from bs4 import BeautifulSoup


def scrape():
    url = "https://www.lemonde.fr/?preferred_lang=fr"
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")

    titles, descs, links = [], [], []

    # --- Main article ---
    main_article = soup.find("div", class_="article--main")
    if main_article:
        a_tag = main_article.find("a", class_="lmd-link-clickarea__link", href=True)
        title_tag = None
        if a_tag:
            title_tag = a_tag.find("p", class_="article__title-label")
        if not title_tag:
            h1_tag = main_article.find("h1", class_="article__title")
            if h1_tag:
                title_tag = h1_tag.find("p", class_="article__title-label") or h1_tag

        desc_tag = main_article.find("p", class_="article__desc")
        href = a_tag["href"] if a_tag else None
        if href and href.startswith("/"):
            href = "https://www.lemonde.fr" + href

        if href and title_tag:
            links.append(href)
            titles.append(title_tag.get_text(strip=True))
            descs.append(desc_tag.get_text(strip=True) if desc_tag else "-")

    # --- Other sections ---
    for cls, has_desc in [
        ("article--headlines", False),
        ("article--runner", True),
        ("article--featured", True),
        ("article--river", False),
    ]:
        for div in soup.find_all(class_=cls):
            a_tag = div.find("a", href=True)
            if not a_tag:
                continue
            href = a_tag["href"]
            if href.startswith("/"):
                href = "https://www.lemonde.fr" + href
            title_tag = div.find("p", class_="article__title") or div.find("h3", class_="article__title")
            desc_tag = div.find("p", class_="article__desc") if has_desc else None

            if title_tag:
                titles.append(title_tag.get_text(strip=True))
                descs.append(desc_tag.get_text(strip=True) if desc_tag else "-")
                links.append(href)

    # Limit to 10
    return titles[:10], descs[:10], links[:10]
