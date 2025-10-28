import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style
import webbrowser


def scrape_lemonde():
    print(f"{Fore.GREEN}Reading LE MONDE...{Style.RESET_ALL}")

    url = "https://www.lemonde.fr/?preferred_lang=fr"
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")

    lm_links, lm_titles, lm_descs = [], [], []

    # --- Main (front live) article ---
    main_article = soup.find("div", class_="article--main")
    if main_article:
        a_tag = main_article.find("a", class_="lmd-link-clickarea__link", href=True)
        title_tag = None

        # Try to extract the title text
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
            lm_links.append(href)
            lm_titles.append(title_tag.get_text(strip=True))
            lm_descs.append(desc_tag.get_text(strip=True) if desc_tag else "-")

    # --- Headline section ---
    for div in soup.find_all(class_="article--headlines"):
        a_tag = div.find("a", href=True)
        title_tag = div.find("p", class_="article__title")

        if not a_tag or not title_tag:
            continue

        href = a_tag["href"]
        if href.startswith("/"):
            href = "https://www.lemonde.fr" + href

        lm_links.append(href)
        lm_titles.append(title_tag.get_text(strip=True))
        lm_descs.append("-")

    # --- Runner section ---
    for div in soup.find_all(class_="article--runner"):
        a_tag = div.find("a", href=True)
        title_tag = div.find("p", class_="article__title")
        desc_tag = div.find("p", class_="article__desc")

        if not a_tag or not title_tag:
            continue

        href = a_tag["href"]
        if href.startswith("/"):
            href = "https://www.lemonde.fr" + href

        lm_links.append(href)
        lm_titles.append(title_tag.get_text(strip=True))
        lm_descs.append(desc_tag.get_text(strip=True) if desc_tag else "-")

    # --- Featured articles ---
    for div in soup.find_all(class_="article--featured"):
        a_tag = div.find("a", href=True)
        title_tag = div.find("p", class_="article__title")
        desc_tag = div.find("p", class_="article__desc")

        if not a_tag or not title_tag:
            continue

        href = a_tag["href"]
        if href.startswith("/"):
            href = "https://www.lemonde.fr" + href

        lm_links.append(href)
        lm_titles.append(title_tag.get_text(strip=True))
        lm_descs.append(desc_tag.get_text(strip=True) if desc_tag else "-")

    # --- River articles ---
    for div in soup.find_all(class_="article--river"):
        a_tag = div.find("a", href=True)
        title_tag = div.find("h3", class_="article__title")

        if not a_tag or not title_tag:
            continue

        href = a_tag["href"]
        if href.startswith("/"):
            href = "https://www.lemonde.fr" + href

        lm_links.append(href)
        lm_titles.append(title_tag.get_text(strip=True))
        lm_descs.append("-")

    # Limit to first 10
    lm_links = lm_links[:10]
    lm_titles = lm_titles[:10]
    lm_descs = lm_descs[:10]

    return lm_titles, lm_descs, lm_links


def main():
    titles, descs, links = scrape_lemonde()

    print(f"\n{Fore.CYAN}--- Found {len(titles)} articles ---{Style.RESET_ALL}\n")
    for i, (title, desc) in enumerate(zip(titles, descs)):
        print(f"{Fore.BLUE}{i + 1}.{Style.RESET_ALL} {Fore.MAGENTA}{title}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}    {desc}{Style.RESET_ALL}\n")

    while True:
        choice = input(f"{Fore.GREEN}Pick an article number (Enter to quit): {Style.RESET_ALL}")
        if not choice:
            break
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(links):
                webbrowser.open(links[idx])
            else:
                print(f"{Fore.RED}Invalid number.{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}Please enter a number.{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
