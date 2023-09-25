import requests
from bs4 import BeautifulSoup
import webbrowser
from colorama import Fore, Style

print("Let's scrap the news")
print('\n')

newspapers = ['Financial Times', 'New Yorker', 'The Economist', 'New York Times']
exit_flag = False

while True:
    for paper in newspapers:
        while True:
            if paper == 'Financial Times':
                print(f'Read the {paper.upper()}')
                ft = requests.get("http://www.ft.com")
                ftsoup = BeautifulSoup(ft.content, "html.parser")
                ftresults = ftsoup.find_all(class_="js-teaser-headline")
                ft_links = []
                ft_title = []

                for div in ftresults[:10]:
                    anchor = div.find('a')
                    if anchor:
                        href = 'https://www.ft.com' + anchor.get('href')
                        text = anchor.get_text(strip=True)
                        if href:
                            ft_links.append(href)
                            ft_title.append(text)

                for i, result in enumerate(ft_title):
                    print(f"{Fore.BLUE}{i + 1} - {Style.RESET_ALL} {Fore.MAGENTA}{result}{Style.RESET_ALL}")

                user_input = input(f"{Fore.GREEN}{Style.BRIGHT}Pick one article, press enter to exit, press x to get to the next newspaper: \n {Style.RESET_ALL}")

                if user_input == '':
                    exit_flag = True
                    break
                elif user_input.lower() == 'x':
                    break
                user_input = int(user_input) - 1
                if 0 <= user_input < len(ft_links):
                    webbrowser.open(ft_links[user_input])
                    continue

            elif paper == 'New Yorker':
                print(f'Read the {paper.upper()}')
                ny = requests.get("https://www.newyorker.com/")
                nysoup = BeautifulSoup(ny.content, "html.parser")
                nyresults = nysoup.find_all(class_="summary-item__hed-link")
                ny_links = []
                ny_titles = []

                for div in nyresults[:10]:
                    if div:
                        href = 'https://www.newyorker.com' + div.get('href')
                        text = div.get_text(strip=True)
                        ny_links.append(href)
                        ny_titles.append(text)

                for i, result in enumerate(ny_titles):
                    print(f"{Fore.BLUE}{i + 1} - {Style.RESET_ALL} {Fore.MAGENTA}{result}{Style.RESET_ALL}")

                user_input = input(f"{Fore.GREEN}{Style.BRIGHT}Pick one article, press enter to exit, press x to get to the next newspaper: \n {Style.RESET_ALL}")

                if user_input == '':
                    exit_flag = True
                    break
                elif user_input.lower() == 'x':
                    break
                user_input = int(user_input) - 1
                if 0 <= user_input < len(ny_links):
                    webbrowser.open(ny_links[user_input])
                    continue

            elif paper == 'The Economist':
                print(f'Read the {paper.upper()}')
                te = requests.get("https://www.economist.com/")
                tesoup = BeautifulSoup(te.content, "html.parser")
                teresults = tesoup.find_all(class_="ekfon2k0")
                te_links = []
                te_titles = []

                for div in teresults[:10]:
                    anchor = div.find('a')
                    if anchor:
                        href = 'https://www.economist.com' + anchor.get('href')
                        text = anchor.get_text(strip=True)
                        if href:
                            te_links.append(href)
                            te_titles.append(text)

                for i, result in enumerate(te_titles):
                    print(f"{Fore.BLUE}{i + 1} - {Style.RESET_ALL} {Fore.MAGENTA}{result}{Style.RESET_ALL}")

                user_input = input(f"{Fore.GREEN}{Style.BRIGHT}Pick one article, press enter to exit, press x to get to the next newspaper: \n {Style.RESET_ALL}")

                if user_input == '':
                    exit_flag = True
                    break
                elif user_input.lower() == 'x':
                    break
                user_input = int(user_input) - 1
                if 0 <= user_input < len(te_links):
                    webbrowser.open(te_links[user_input])
                    continue

            elif paper == 'New York Times':
                print(f'Read the {paper.upper()}')
                nytimes = requests.get("https://www.nytimes.com/")
                nysoup = BeautifulSoup(nytimes.content, "html.parser")
                nytimes_results = nysoup.find_all(class_="css-9mylee")
                nytimes_links = []
                nytimes_titles = []

                for div in nytimes_results[:10]:
                    if div:
                        nested_div = div.find(class_="css-xdandi")

                        if nested_div:
                            text = nested_div.get_text(strip=True)
                            nytimes_titles.append(text)

                            href = div.get('href')
                            if href:
                                nytimes_links.append(href)

                for i, result in enumerate(nytimes_titles):
                    print(f"{Fore.BLUE}{i + 1} - {Style.RESET_ALL} {Fore.MAGENTA}{result}{Style.RESET_ALL}")

                user_input = input(f"{Fore.GREEN}{Style.BRIGHT}Pick one article, press enter to exit, press x to get back to the first newspaper: \n {Style.RESET_ALL}")

                if user_input == '':
                    exit_flag = True
                    break
                elif user_input.lower() == 'x':
                    break
                user_input = int(user_input) - 1
                if 0 <= user_input < len(nytimes_links):
                    webbrowser.open(nytimes_links[user_input])
                    continue

        if exit_flag:
            break

    if exit_flag:
        print("Goodbye!")
        break
