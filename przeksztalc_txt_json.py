!/usr/bin/env python3

import requests
import os


url = "http://35.237.230.135/fruits/"
path2 = os.getcwd() + "/supplier-data/images/"
path = os.getcwd() + "/supplier-data/descriptions/"
lista = os.listdir(path)
slownik = {}
lista_slownika = []
lista_owocow = []
for opis in lista:
  with open(path + opis, "r") as file:
    data = file.read()
    line = data.strip().split("\n")
#   print(line)
    for lines in line:
      if "lbs" in lines:
        wgh = lines.split()
#        print(wgh)
        slownik = {
        'name' : line[0],
        'weight' : int(wgh[0]),
        'description' : line[2],
        'image_name' : opis
        }
        lista_slownika.append(slownik)
        name = slownik['image_name']
        name_l = name.split(".")
        name_f = name_l[0] + ".jpeg"
        for images in os.listdir(path2):
          if images == name_f:
            slownik['image_name'] = images
            print(slownik)
            response = requests.post(url, json=slownik) 
