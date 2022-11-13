#!/usr/bin/python3

import requests
import sys

sub_list = open("wordlist.txt").read()
dir = sub_list.splitlines()
print("[+] Scanning...")

for d in dir:
    dir_enum = f"http://{sys.argv[1]}/{d}.html"
    r = requests.get(dir_enum)
    if r.status_code==404:
        pass
    else:
        print("Valid directory: ",dir_enum)
