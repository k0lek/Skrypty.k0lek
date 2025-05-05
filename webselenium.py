from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import time
import re
from bs4 import BeautifulSoup
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from datetime import datetime
from reportlab.lib.styles import getSampleStyleSheet  # Dodaj tę linię
# Konfiguracja Firefoksa
options = Options()
options.headless = True  # Uruchomienie w tle (usuń, jeśli chcesz widzieć przeglądarkę)

# Uruchomienie Firefoksa
service = Service("/snap/bin/geckodriver") 
driver = webdriver.Firefox(service=service, options=options)

# Otwórz stronę
driver.get("https://nbp.pl/statystyka-i-sprawozdawczosc/kursy/tabela-a/")

time.sleep(2)
html = driver.page_source
# Pobierz tytuł strony
#przekazujemy html do soup
# Zamknij przeglądarkę
driver.quit()
soup = BeautifulSoup(html, "lxml")
sas = soup.find_all('td')
slownik = {}
le = []
for i in range(0, len(sas), 3):
  nazwa = sas[i].text.strip()
  ilosc = sas[i+1].text.strip()
  kurs = sas[i+2].text.strip()
  
  slownik[nazwa] = ilosc, kurs
  
today_date = datetime.now().strftime("%d %B %Y") 
# Tworzenie dokumentu PDF
pdf_filename = "raport_walutowy" + today_date + ".pdf"
doc = SimpleDocTemplate("raporty_pdf/" + pdf_filename, pagesize=letter)
# Rejestracja czcionki z obsługą polskich znaków (FreeSerif)
pdfmetrics.registerFont(TTFont('FreeSerif', '/usr/share/fonts/truetype/freefont/FreeSerif.ttf'))
# Nagłówki tabeli
data = [["Waluta", "Ilość", "Kurs"]]
# Dodawanie danych do tabeli
for nazwa, dane in slownik.items():
    data.append([nazwa, dane[0], dane[1]])
# Tworzenie tabeli
table = Table(data)
# Stylowanie tabeli
style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Tło nagłówka
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Kolor tekstu nagłówka
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Wyrównanie tekstu
    ('FONTNAME', (0, 0), (-1, 0), 'FreeSerif'),  # Czcionka nagłówka
    ('FONTNAME', (0, 1), (-1, -1), 'FreeSerif'),  # Czcionka dla reszty tabeli
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Odstęp wierszy
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  # Tło wierszy
    ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Ramki tabeli
])
# Zastosowanie stylu do tabeli
table.setStyle(style)
elements = []
# Pobranie stylów do Paragraph
styles = getSampleStyleSheet()  # Dodaj tę linię
date_paragraph = Paragraph(f"Data wygenerowania raportu: {today_date}<br/><br/>", styles['Normal'])
elements.append(date_paragraph)
# Dodawanie tabeli do dokumentu PDF
elements.append(table)

# Budowanie dokumentu
doc.build(elements)

print(f"Raport PDF został zapisany jako {pdf_filename}")
  

