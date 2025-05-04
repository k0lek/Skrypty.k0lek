
#! /usr/bin/env python3

import os
import requests

content = ""
path = "/data/feedback/"
filenames = os.listdir(path)
slownik_lista = []
for file_name in filenames:
  file_path = os.path.join(path + file_name)
  with open(file_path, "r", encoding='utf8', newline='\n') as txt:
    slownik = {}
    lines = txt.readlines()
    slownik['title'] = lines[0].strip()
    slownik['name'] = lines[1].strip()
    slownik['date'] = lines[2].strip()
    slownik['feedback'] = lines[3].strip()
    slownik_lista.append(slownik)
url = "http://34.168.206.240/feedback/"
response = requests.get(url)
if response.ok:
  for lista in slownik_lista:
    response1 = requests.post(url, json=lista)
    if response1.ok:
      print(response1.text)
