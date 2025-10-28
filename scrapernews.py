# main.py
import importlib
import webbrowser
from colorama import Fore, Style

newspapers = {
    'Financial Times': 'financial_times',
    'New Yorker': 'new_yorker',
    'Atlantic': 'atlantic',
    'New York Times': 'new_york_times',
    'Le Monde': 'le_monde',
    'The Guardian': 'guardian',
}

print(f"{Fore.GREEN}Let's read the news!{Style.RESET_ALL}")

while True:
    print('\n' + '_'*10)
    for i, paper in enumerate(newspapers):
        print(f"{Fore.BLUE}{i + 1} - {Style.RESET_ALL}{Fore.MAGENTA}{paper}{Style.RESET_ALL}")
    print('_'*10)

    user_input = input(f"{Fore.GREEN}Pick a newspaper by number or 'x' to exit:\n> {Style.RESET_ALL}")

    if user_input.lower() == 'x':
        print("Goodbye!")
        break

    try:
        idx = int(user_input) - 1
        if not (0 <= idx < len(newspapers)):
            raise ValueError
        paper_name = list(newspapers.keys())[idx]
        module_name = newspapers[paper_name]
    except ValueError:
        print("Invalid input.")
        continue

    print(f"\n{Fore.CYAN}Reading {paper_name.upper()}...{Style.RESET_ALL}")

    try:
        scraper = importlib.import_module(f"papers.{module_name}")
        titles, descs, links = scraper.scrape()
    except Exception as e:
        print(f"{Fore.RED}Error loading {paper_name}: {e}{Style.RESET_ALL}")
        continue

    if not titles:
        print("No articles found.")
        continue

    while True:
        for i, (title, desc) in enumerate(zip(titles, descs)):
            print(f"{Fore.BLUE}{i + 1}.{Style.RESET_ALL} {Fore.MAGENTA}{title}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}    {desc}{Style.RESET_ALL}\n")

        choice = input(f"{Fore.GREEN}Pick an article number, Enter to go back the the newspaper list, or x to exit:\n> {Style.RESET_ALL}")

        if choice.lower() == 'x':
            exit()
        elif not choice:
            break
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(links):
                webbrowser.open(links[idx])
                print("Opened in browser.")
            else:
                print("Invalid number.")
        except ValueError:
            print("Enter a valid number.")
