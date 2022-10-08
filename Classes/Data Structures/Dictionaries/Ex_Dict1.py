person1 = {'firstname': 'John', 'lastname': 'Smith', 'age': 42}
person2 = dict(firstname='John', lastname='Smith', age=42)
person1['gender'] = 'male'
person1['telephone'] = '3528-7564'

print(person1)
print(person2)
print(person1['firstname'])
print(person2['lastname'])

person2['firstname'] = 'Lisa'
person2['lastname'] = 'Kennedy'
person2['age'] = 28
person2['gender'] = 'female'
person2['telephone'] = '99528-7004'

print(person1)
print(person2)

contacts = {
    'johnsmith@gmail.com': {'name': {'firstname': 'John', 'lastname': 'Smith'}, 'age': 42, 'telephones': {'home': '3546-8962', 'cel': '99866-3560'}},
    'lisakennedy@gmail.com': {'name': {'firstname': 'Lisa', 'lastname': 'Kennedy'}, 'age': 28, 'telephones': {'home': '3528-0032', 'cel': '99528-7004'}},
}

celphone = contacts['johnsmith@gmail.com']['telephones']['home']
print(celphone)

for key in contacts:
    print(key, contacts[key])

for key, value in contacts.items():
    print(key, value)