#!/usr/bin/python3

import re
import numpy

def otworz(plik):
  with open(plik, "r", encoding='utf8') as f:
    reader = f.read()
  return reader


def wyszukaj(tekst):

 wyszukuje = re.compile(r"error.*")
 lista = wyszukuje.findall(tekst)
 return lista
1

figa = otworz("przyklad2.txt")
gruszka = wyszukaj(figa)
for i in gruszka:
  print(i)

