#! /usr/bin/env python3
import random
import string

def start():
    try:
        with open("EncryptionKey.txt", "r") as f:
            key = f.read()
    except FileNotFoundError:
        with open("EncryptionKey.txt", "w") as f:
            f.write(''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in range(256)]))
        with open("EncryptionKey.txt", "r") as f:
            key = f.read()
    return key

def choose(key):
    while True:
        enter = input("""
Choose what action to preform:
1. Encode message
2. Decode message
3. Generate new key
4. End Program
""")
        if enter == "1":
            encode(key)
        elif enter == "2": 
            decode(key)
        elif enter == "3":
            key = generate()
        elif enter == "4":
            break
        else:
            print("Invalid option")

def encode(key):
    shift = 0
    solved = ""
    org_txt = input("Enter the text you want to encode:\n")
    for char in org_txt:
        cur_en = ord(char) - ord("!")
        cur_key = ord(key[shift]) - ord("!")
        if shift < len(key)-1:
            shift += 1
        else:
            shift = 0
        solv_cur = (cur_key + cur_en) % 93
        solved += chr(solv_cur + ord("!"))

    print(solved)

def decode(key):
    shift = 0
    solved = ""

    org_txt = input("Enter the text you want to decode:\n")
    for char in org_txt:
        cur_de = ord(char) - ord("!")
        cur_key = ord(key[shift]) - ord("!")
        if shift < len(key)-1:
            shift += 1
        else:
            shift = 0
        solv_cur = (cur_de - cur_key) %  93
        solved += chr(solv_cur + ord("!"))

    print(solved)

def generate():
    with open("EncryptionKey.txt", "w") as f:
        f.write(''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in range(256)]))
    with open("EncryptionKey.txt", "r") as f:
        key = f.read()
    print("New key generated")
    return key

def main():
    encKey :str = ""
    encKey = start()
    choose(encKey)

main()
