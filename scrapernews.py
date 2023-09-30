import requests
from bs4 import BeautifulSoup
import webbrowser
from colorama import Fore, Style

print("Let's scrap the news")

newspapers = ['Financial Times', 'New Yorker', 'The Economist', 'New York Times', 'Le Monde']
exit_flag = False

should_print_titles = True

while True:
    if should_print_titles:
        print('_'*10)
        print('\n')
        for i, paper in enumerate(newspapers):
            print(f"{Fore.BLUE}{i + 1} - {Style.RESET_ALL} {Fore.MAGENTA}{paper}{Style.RESET_ALL}")
        print('\n')
        print('_'*10)

    user_input = input(f"{Fore.GREEN}{Style.BRIGHT}Pick a newspaper by number or type 'x' to exit:\n > {Style.RESET_ALL}")

    should_print_titles = True

    if user_input.lower() == 'x':
        print("Goodbye!")
        break
    try:
        user_input = int(user_input) - 1
        if 0 <= user_input < len(newspapers):
            pass
        else:
            print("Type a valid number")
            should_print_titles = False
            continue
    except ValueError:
        print("Type a valid command")
        should_print_titles = False
        continue

    # Step 3 - Switch Logic
    paper = newspapers[user_input]

    if paper == 'Financial Times':
        print(f'Read the {paper.upper()}')
        ft = requests.get("http://www.ft.com")
        ftsoup = BeautifulSoup(ft.content, "html.parser")
        ftresults = ftsoup.find_all(class_="js-teaser-headline")
        ft_links = []
        ft_title = []
        ft_description = []

        for div in ftresults[:10]:
            anchor = div.find('a')
            if anchor:
                href = 'https://www.ft.com' + anchor.get('href')
                text = anchor.get_text(strip=True)
                if href:
                    ft_links.append(href)
                    ft_title.append(text)

        should_print_list = True  # Initialize the control flag

        while True:
            if should_print_list:  # Check if the list needs to be printed
                for i, result in enumerate(ft_title):
                    print(f"{Fore.BLUE}{i + 1} - {Style.RESET_ALL} {Fore.MAGENTA}{result}{Style.RESET_ALL}")

            user_input = input(f"{Fore.GREEN}{Style.BRIGHT}Pick one article, press enter to choose another newspaper, or press x to exit: \n > {Style.RESET_ALL}")

            if user_input.lower() == 'x':
                exit_flag = True
                break
            elif user_input.lower() == '':
                break
            try:
                user_input = int(user_input) - 1
                if 0 <= user_input < len(ft_links):
                    webbrowser.open(ft_links[user_input])
                    should_print_list = False  # Set flag to false; no need to print the list
                else:
                    print('Type a valid number, or type x to exit  \n >')
                    should_print_list = False  # Set flag to false; no need to print the list
            except ValueError:
                print('Type a valid command, or type x to exit  \n >')
                should_print_list = False  # Set flag to true; print the list again


    elif paper == 'New Yorker':
        print(f'Read the {paper.upper()}')
        ny = requests.get("https://www.newyorker.com/")
        nysoup = BeautifulSoup(ny.content, "html.parser")
        nyresults = nysoup.find_all(class_="summary-item__hed-link")
        ny_links = []
        ny_titles = []
        ny_descriptions = []

        for div in nyresults[:10]:
            if div:
                href = 'https://www.newyorker.com' + div.get('href')
                text = div.get_text(strip=True)
                ny_links.append(href)
                ny_titles.append(text)

        for link in ny_links:  # Looping through all links
            article_page = requests.get(link)  # Fetching the article
            article_soup = BeautifulSoup(article_page.content, 'html.parser')  # Parsing the article HTML
            description_divs = article_soup.find_all(class_=["ContentHeaderDek-bIqFFZ", "SplitScreenContentHeaderDek-emptdL"])

            if description_divs:
                for div in description_divs:
                    description = div.get_text(strip=True)
                    ny_descriptions.append(description)
            else:
                ny_descriptions.append('Description not found')


        for i, (title, description) in enumerate(zip(ny_titles, ny_descriptions)):
            print(f"{Fore.BLUE}{i + 1} - {Style.RESET_ALL} {Fore.MAGENTA}{title}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW} - {Style.RESET_ALL} {Fore.WHITE}{description}{Style.RESET_ALL}")

        user_input = input(f"{Fore.GREEN}{Style.BRIGHT}Pick one article, press enter to get to the next newspaper, or press x to exit: \n {Style.RESET_ALL}")

        if user_input.lower() == 'x':
            exit_flag = True
            break
        elif user_input == '':
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

        user_input = input(f"{Fore.GREEN}{Style.BRIGHT}Pick one article, press enter to get to the next newspaper, or press x to exit: \n {Style.RESET_ALL}")

        if user_input.lower() == 'x':
            exit_flag = True
            break
        elif user_input == '':
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
        nytimes_descriptions = []

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

        if user_input.lower() == 'x':
            exit_flag = True
            break
        elif user_input == '':
            break
        user_input = int(user_input) - 1
        if 0 <= user_input < len(nytimes_links):
            webbrowser.open(nytimes_links[user_input])
            continue

    elif paper == 'Le Monde':
        print(f'Read the {paper.upper()}')
        lm = requests.get("https://www.lemonde.fr/")
        lmsoup = BeautifulSoup(lm.content, "html.parser")
        lmresults = lmsoup.find_all(class_="article")
        lm_links = []
        lm_titles = []


        for div in lmresults[:10]:
            href = div.get('href')
            text = div.get_text(strip=True)
            if href:
                lm_links.append(href)
                lm_titles.append(text)


        for i, result in enumerate(lm_titles):
            print(f"{Fore.BLUE}{i + 1} - {Style.RESET_ALL} {Fore.MAGENTA}{result}{Style.RESET_ALL}")

        user_input = input(f"{Fore.GREEN}{Style.BRIGHT}Pick one article, press enter to exit, press x to get back to the first newspaper: \n {Style.RESET_ALL}")

        if user_input.lower() == 'x':
            exit_flag = True
            break
        elif user_input == '':
            break
        user_input = int(user_input) - 1
        if 0 <= user_input < len(lm_links):
            webbrowser.open(lm_links[user_input])
            continue

        if exit_flag:
            break

    if exit_flag:
        print("Goodbye!")
        break




# in Le Monde fetching article only gets the header; find another class for the mainpage articles
