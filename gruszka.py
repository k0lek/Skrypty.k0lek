#!/usr/bin/python3

import re
import numpy
import logging
import inspect
import os

logging.basicConfig(filename='logi.log', level=logging.INFO)
log = logging.getLogger(os.path.basename(__file__))

def otworz(plik):
  with open(plik, "r", encoding='utf8') as f:
    reader = f.read()
    log.info("Otwieram plik")
  return reader


def wyszukaj(tekst):

  wyszukuje = re.sub(r"(\S{3}\s\S{2}\s\S{8})\s\S{15}\s(.*)", "\g<2>", tekst)
  log.info("Przetwarzam dane")
  return wyszukuje

def main():

  figa = otworz("przyklad2.txt")
  gruszka = wyszukaj(figa)


if __name__ == '__main__':
  main()
