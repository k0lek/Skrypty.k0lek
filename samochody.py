#!/usr/bin/env python3

import json
import collections
import locale

try:
  with open("samochody.txt", "r") as file:
    data = json.load(file)
except Exception as e:
  print(f"(wystąpił błąd {e}")
"""Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """
max_revenue = {'revenue': 0}
car = {'total_sales': 0}
car_year_sales = collections.defaultdict(int)
for files in data:
  item_price = float(files['price'].strip("$"))
  total_sales_price = item_price * files['total_sales']
  if total_sales_price > max_revenue['revenue']:
    files['revenue'] = total_sales_price
    if files['revenue'] > max_revenue['revenue']:
      max_revenue['revenue'] = files['revenue']
      max_revenue['car'] = files['car']['car_make']
  if files['total_sales'] > car['total_sales']: 
    car['total_sales'] = files['total_sales']
    car_year_sales[files['car']['car_year']] += files['total_sales']
  #if files['price'] > ma#
  # max_revenue = files
  if car['total_sales'] == files['total_sales']:
    car = files
max_car_sales_year = (0,0)
for year, sales in car_year_sales.items():
  if sales > max_car_sales_year[1]:
    max_car_sales_year = (year, sales)
print(max_revenue)


summary = ["Najwieksza sprzedaz byla samochodu firmy {} modelu {} z roku {}. Najbardziej popularny rok sprzedaży to {} ze sprzedażą {}. Najlepszy samochód to {} ze sprzedażą {}.".format(car['car']['car_make'], car['car']['car_model'], car['car']['car_year'], max_car_sales_year[0], max_car_sales_year[1], max_revenue['car'], max_revenue['revenue'])]
print(summary)


