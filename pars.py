import re
import os
import csv
import pandas
# Funkcja otworz() otwiera plik z kodowaniem, czyta jego zawartość i zapisuje do str('tekst').

def otworz(plik):
  tekst = ""
  with open(plik, "r", encoding='windows-1250', newline='\n') as f:
    #file = csv.reader(f)
    #for x in file:
    #  tekst += str(x)
    return f.read()

  return f.read()

# Funkcja szukaj() to algorytm parsowania danych. Zwraca list(wynik)

def szukaj(tekst):

  #wzor1 = r"~38PL\d{1,}"
  wzor1 = r"~38(PL\d+)?"
  wzor2 = r"~20(\w+\D+)?"
  wzor3 = r":61:(\d{6})?" 
  #wzor4 = r":61:\d{10}(\.*)?"
  wzor4 = r":61:\d{10}.(\d+,\d+)?"
  wynik1 = re.findall(wzor1, tekst)
  wynik2 = re.findall(wzor2, tekst)
  wynik3 = re.findall(wzor3, tekst)
  wynik4 = re.findall(wzor4, tekst)
  return wynik1, wynik2, wynik3, wynik4

# Funkcja licz() zwraca ilość wyniku.

def licz(wynik1, wynik2, wynik3):
  ilosc1 = len(wynik1)
  ilosc2 = len(wynik2)
  ilosc3 = len(wynik3)
  return ilosc1, ilosc2, ilosc3

# Funkcja zrob_liste() tworzy liste z wyniku.

def przerob_date(wynik3):
  strin = ""
  for x in wynik3:
    strin = x[:2] + "-" + x[2:4] + "-" + x[4:6]
  #return [f"{str(x)[:2]}-{str(x)[2:4]}-{str(x)[4:6]}" for x in wynik3]
  return strin
  
# Funkcja segreguj_wynik wypisuje przejżyście wynik.

def segreguj_wynik(wynik2):
  licznik = 0
  for kto in wynik2:
    print(kto)
    licznik += 1
  return licznik

# Funkcja main() wykonuje główny cykl programu.

def main():
  tekst = otworz("mt940.txt")
  print(tekst)
  wynik1, wynik2, wynik3, wynik4 = szukaj(tekst)
  ilosc1, ilosc2, ilosc3 = licz(wynik1, wynik2, wynik3)
  data = przerob_date(wynik3)
  df = pandas.DataFrame( {"numery": wynik1, "opis": wynik2, "data": data, "kwota": wynik4})
  pandas.set_option('display.max_rows', None)
  pandas.set_option('display.max_columns', None)
  print(df)
  #print(wynik4)
  print("posegregowane")
  print("Ilość:" + str(ilosc2))

main()
