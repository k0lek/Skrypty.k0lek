import requests
params = {"q": "cats"}
#response = requests.get('https://catpaw.pl/wp-content/uploads/2024/09/Kot-Europjeski.png')
data = {"key": "value", "search": "cats"}
#response = requests.post('https://catpaw.pl/wp-content/uploads/2024/09/Kot-Europjeski.png', data=data)
r = requests.get('https://httpbin.org/get', params=data)
y = requests.delete('https://httpbin.org/delete')
#print(response.text[:300])
#print(response.raw.read()[:100])
#print(response.request.headers['Accept-Encoding'])
#print(response.headers['Content-Encoding'])
#print(response.ok)
#print(response.status_code)
#print(response.raise_for_status())
if r.ok:

  print("wysyłany URL:", r.request.url)
  print(r.headers)
  print("\n", r.request.body)
  print(r.text)
  print(y.status_code)
  print(y.json())
else:
  print("Blad zapytania:", response.status_code)
