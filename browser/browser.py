import sys
import os
import requests
from colorama import init, Fore
from bs4 import BeautifulSoup

stack = []


def create_dir():
    """Create a directory for pages."""
    try:
        dir_name = sys.argv[1]
    except IndexError:
        dir_name = "temp"
    try:
        os.mkdir(dir_name)
    except FileExistsError:
        pass
    return dir_name


def full_url(url):
    """Return full url."""
    if url.startswith("https://"):
        return url
    else:
        return "https://" + url


def get_status(url):
    """Return status (True/False)."""
    try:
        requests.get(url)
    except:
        return False
    return True


def get_cache(url):
    """Return text."""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    page_text = [tags.get_text() for tags in soup.find_all('a')]
    return page_text


def cache_url(dir_name: str, url: str, cache: str):
    """Return cache, make a cache file."""
    full_path = dir_name + "/" + url[:url.rindex(".")] + ".txt"
    with open(full_path, "w", encoding="utf-8") as f:
        text = ''
        for string in cache:
            text = text + Fore.BLUE + string + "\n"
        f.write(text)
    with open(full_path, "r") as f:
        cache = f.read()
    stack.append(cache)
    return cache


def read_cached_url(dir_name: str, url: str):
    """Read cached file."""
    full_path = dir_name + "/" + url + ".txt"
    with open(full_path, "r") as f:
        cache = f.read()
    stack.append(cache)
    return cache


def back():
    """Return back."""
    if len(stack) > 1:
        print(stack.pop(-2))
    else:
        print("Can't go back.")


def main():
    """Main function."""
    init()
    dir_name = create_dir()
    user_input = ""
    while user_input != "exit":
        user_input = input("> ")
        if user_input == "exit":
            continue
        elif user_input == "back":
            back()
            continue
        url = full_url(user_input)
        if get_status(url):
            cache: list = get_cache(url)
            print(cache_url(dir_name, user_input, cache))
        else:
            try:
                print(read_cached_url(dir_name, user_input))
            except FileNotFoundError:
                print("ConnectionError")


if __name__ == "__main__":
    main()
