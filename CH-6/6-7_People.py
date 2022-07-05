people = []
person = {
    'first_name': 'Khair',
    'last_name': 'Ahamed',
    'age': 28,
    'city': 'Chittagong',
}
people.append(person)

person = {
    'first_name': 'Faisal',
    'last_name': 'Ahammed',
    'age': 24,
    'city': 'Dhaka',
}
people.append(person)

person = {
    'first_name': 'rahat',
    'last_name': 'azad',
    'age': '29',
    'city': 'ranguniya',
}
people.append(person)

#print(people)

for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city'].title()

    print(f"{name}, of {city}, is {age} years old.")