people = [
    {"name": "Kama", "home": "Katowice"},
    {"name": "Mama", "home": "Łodygowice"},
    {"name": "Przemek", "home": "Górne"},
]


def f(person):
    return person["name"]


people.sort(key=lambda person: person["name"])
print(people)
