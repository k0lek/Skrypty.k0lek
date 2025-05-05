import re
import requests
from bs4 import BeautifulSoup
import datetime

current_time = datetime.datetime.now()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}


# 1. Wysłanie zapytania GET do strony
#url0 = input()
url = "https://www.orlen.pl/pl/dla-biznesu/hurtowe-ceny-paliw"
response = requests.get(url, headers=headers)

# Sprawdzenie, czy zapytanie się powiodło
if response.status_code == 200:
    print("Strona została pobrana!")
else:
    print(f"Coś poszło nie tak! Status: {response.status_code}")

# 2. Parsowanie HTML przy pomocy BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# 3. Wyciąganie danych (np. tytuł strony)

kurs = soup.find_all('table')
with open("kursy.log", "w") as f:
  f.write(response.text)
  
