import json
people2 = [{'nazwa':'Janosik', 'klucz': 'był chłopem'}]
people = [
  {
    "name": "Sabrina Green",
    "username": "sgreen",
    "phone": {
      "office": "802-867-5309",
      "cell": "802-867-5310"
    },
    "department": "IT Infrastructure",
    "role": "Systems Administrator"
  },
  {
    "name": "Eli Jones",
    "username": "ejones",
    "phone": {
      "office": "684-348-1127"
    },
    "department": "IT Infrastructure",
    "role": "IT Specialist"
  }
]
people_json = json.dumps(people)
people_json2 = json.dumps(people2)
print(people_json)
print(people2)
with open('people.json', 'w') as people_json:
    json.dump(people, people_json, indent=2)
    json.dump(people2, people_json2, indent=2)
