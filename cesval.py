#!/usr/bin/env python3
import csv
import os
import string
import secrets

def haslo(ilosc):

  symbol = ""

  for i in range(ilosc):
    symbol += secrets.choice(string.digits)
    symbol += " "
    symbol += secrets.choice(string.ascii_letters)
    symbol += " "
    symbol += secrets.choice(string.punctuation)
    symbol += " "
    
  
  
  return symbol
    
print(haslo(3))
