import sys
import time
import string
import zipfile
import itertools


file_name = "file.zip"
start_time = 0.0


def crack_zip(pwd):
    try:
        with zipfile.ZipFile(file_name) as file:
            file.extractall(pwd=bytes(pwd, 'utf-8'))
            print(f"[+]  Found Password: {pwd}")
            print(f"[*]  Runtime: {time.time() - start_time}")
            sys.exit()
    except Exception:  # That excludes the raised 'SystemExit' by sys.exit()
        pass


def main():
    global start_time
    min_characters = 1
    max_characters = 10
    wordlist_characters = string.digits  # string.ascii_letters + string.punctuation + " "
    print("[*]  Cracking")
    start_time = time.time()
    for i in range(min_characters, max_characters):
        for j in map(''.join, itertools.product(wordlist_characters, repeat=i)):
            crack_zip(j)
    print("[-]  No password found")


if __name__ == '__main__':
    main()
