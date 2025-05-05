#!/usr/bin/python3

import re
import logging
import os
logging.basicConfig(filename='logi.log', level=logging.INFO)
log = logging.getLogger(os.path.basename(__file__))
def otworz(plik):
  with open(plik, "r", encoding='utf8') as f:
    reader = f.read()
    log.info("otwieram plik")
  return reader


def wyszukaj(figa):

  wzor = r"^(.*error.*)$"
  odp = re.findall(wzor, figa, re.MULTILINE | re.IGNORECASE)
  log.info("Przetwarzam plik")
  return odp
  
def zapisz(plik, wzorek):

  with open(plik, "w", encoding='utf-8') as f:
    for i in wzorek:
      f.write(i)
      f.write("\n\n")
    log.info("zapisuje")
  return print("Zapisano i zamknięto")
  
def main():
  figa = otworz("wynik.txt")
  wzorek = wyszukaj(figa)
  zapisz("wynik2.txt", wzorek)

if __name__ == '__main__':
  main()
