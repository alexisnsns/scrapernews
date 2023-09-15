import requests
from bs4 import BeautifulSoup
import webbrowser
from colorama import Fore, Back, Style, init

print("Let's scrap the news")
print('\n')
print('Here are the 10 first articles of the FT')

# FT
# while True:
#     print('\n')
#     ft = requests.get("http://www.ft.com")
#     ftsoup = BeautifulSoup(ft.content, "html.parser")
#     ftresults = ftsoup.find_all(class_="js-teaser-headline")
#     ft_links = []
#     ft_title = []

#     # Append title and link to arrays
#     for div in ftresults[:10]:
#         anchor = div.find('a')
#         if anchor:
#             href = 'https://www.ft.com' + anchor.get('href')
#             text = anchor.get_text(strip=True)
#             if href:
#                 ft_links.append(href)
#                 ft_title.append(text)

#     for i, result in enumerate(ft_title):
#         print(f"{Fore.BLUE}{i + 1} - {Style.RESET_ALL} {Fore.MAGENTA}{result}{Style.RESET_ALL}")

#     user_input = input(f"{Fore.GREEN}{Style.BRIGHT}Pick one article, press enter to exit, press x to get to the next page: \n {Style.RESET_ALL}")

#     if user_input == '':
#         break
#     user_input = int(user_input) - 1
#     if 0 < user_input < len(ft_links):
#         webbrowser.open(ft_links[user_input])
#     else:
#         print("Please select a valid article number")

# print("Goodbye!")


# NYT
print('\n')
nyt = requests.get("https://www.nytimes.com/")
nytsoup = BeautifulSoup(nyt.content, "html.parser")
nytresults = nytsoup.find_all('h3')
nyt_titles = []

for h3_tag in nytresults:
    nyt_titles.append(h3_tag.get_text())

print(nyt_titles)


# for h3 in nytresults[:10]:
#     anchor = h3.find('a')
#     if anchor:
#         href = 'https://www.ft.com' + anchor.get('href')
#         text = anchor.get_text(strip=True)
#         if href:
#             ft_links.append(href)
#             ft_title.append(text)

    # for i, result in enumerate(ft_title):
    #     print(f"{Fore.BLUE}{i + 1} - {Style.RESET_ALL} {Fore.MAGENTA}{result}{Style.RESET_ALL}")

    # user_input = input(f"{Fore.GREEN}{Style.BRIGHT}Pick one article, press enter to exit, press x to get to the next page: \n {Style.RESET_ALL}")

    # if user_input == '':
    #     break
    # user_input = int(user_input) - 1
    # if 0 < user_input < len(ft_links):
    #     webbrowser.open(ft_links[user_input])
    # else:
    #     print("Please select a valid article number")






# grab overall class, within it find href and title. same as FT. try to do it clean before getting to the desc.
