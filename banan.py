#!/usr/bin/python3

import re


def otworz(plik):
  with open(plik, "r", encoding='utf8') as f:
    reader = f.read()
  return reader


def wyszukaj(figa):

  wzor = r"^(Dec 22.*)$"
  odp = re.findall(wzor, figa, re.MULTILINE | re.IGNORECASE)
  return odp
  
def zapisz(plik, wzorek):

  with open(plik, "w", encoding='utf-8') as f:
    for i in wzorek:
      f.write(i)
      f.write("\n\n")
  return print("Zapisano i zamknięto")
  
figa = otworz("syslog")
wzorek = wyszukaj(figa)
zapisz("wynik.txt", wzorek)

