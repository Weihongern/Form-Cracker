import requests
import random


def main():
    print("Google Form URL")
    url = input(":")
    r = requests.get(url)
    if r.ok:
        print("URL is valid!")
    else:
        print("Error: Get URL Response Failed!")
        return

    print("How many of item inside your URL?")
    print("Example: https://docs.google.com/forms/d/testformj")
    items = int(input(":"))

    url += "/formResponse"

    for item in range(items):
        item = 1
        if item == 1:
            print("Item 1 first one need edit to '?' (&>?)")
        print(f"Enter item {item} data")
        text = input(":")
        url += text
        item += 1

    time = int(input("Enter request range:"))


    print("It's time to do something interesting...")
    print("Start sending data...")

    for i in range(time):
        r = requests.get(url)
        n = 1
        if r.ok:
            print(f"Response Range: {n}")
            print("Send item working!")
        else:
            print(f"Response Range {n} Failed!")
            print("Please Check your item are entered correctly!")
            return
        n += 1



if __name__ == '__main__':
    main()
