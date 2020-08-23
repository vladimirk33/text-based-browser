import sys
import os

stack = []

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''


def is_valid_url(url):
    if "." in url:
        return True
    return False


def create_dir():
    try:
        dir_name = sys.argv[1]
    except IndexError:
        dir_name = "temp"
    try:
        os.mkdir(dir_name)
    except FileExistsError:
        pass
    return dir_name


def cache_url(dir_name: str, url: str, cache: str):
    full_path = dir_name + "/" + url[:url.rindex(".")] + ".txt"
    with open(full_path, "w") as f:
        f.write(cache)
    stack.append(cache)


def read_cached_url(dir_name: str, url: str):
    full_path = dir_name + "/" + url + ".txt"
    with open(full_path, "r") as f:
        cache = f.read()
    stack.append(cache)
    return cache


def back():
    if len(stack) > 1:
        print(stack.pop(-2))
    else:
        print("Can't go back.")


def main():
    dir_name = create_dir()
    user_input = ""
    while user_input != "exit":
        user_input = input("> ")
        if is_valid_url(user_input):
            if user_input == "nytimes.com":
                cache_url(dir_name, user_input, nytimes_com)
                print(nytimes_com)
            elif user_input == "bloomberg.com":
                cache_url(dir_name, user_input, bloomberg_com)
                print(bloomberg_com)
            else:
                print("Error: Incorrect URL")
        else:
            if user_input == "exit":
                pass
            elif user_input == "back":
                back()
            else:
                try:
                    print(read_cached_url(dir_name, user_input))
                except FileNotFoundError:
                    print("Error: Incorrect URL")


if __name__ == "__main__":
    main()
