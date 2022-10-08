# Method copy
person1 = {'firstname': 'John', 'lastname': 'Smith', 'age': 42}
print(type(person1))
print(person1)
person2 = person1.copy()
print(person2)

print('-----------------------------------------------------------------------------')
# Method clear
person1.clear()
print(person1)
print(person2)

print('-----------------------------------------------------------------------------')
# Method fromkeys
person = dict.fromkeys(['firstname', 'lastname', 'gender', 'age', 'email', 'phone'])
print(person)
person = dict.fromkeys(['firstname', 'lastname', 'gender', 'age', 'email', 'phone'], 'empty')
print(person)

print('-----------------------------------------------------------------------------')
# Method get
contacts = {
    'johnsmith@gmail.com': {'name': {'firstname': 'John', 'lastname': 'Smith'}, 'age': 42, 'telephones': {'home': '3546-8962', 'cel': '99866-3560'}},
    'lisakennedy@gmail.com': {'name': {'firstname': 'Lisa', 'lastname': 'Kennedy'}, 'age': 28, 'telephones': {'home': '3528-0032', 'cel': '99528-7004'}},
}

print(contacts.get('key'))
print(contacts.get('key', {}))
print(contacts.get('johnsmith@gmail.com', {}))

print('-----------------------------------------------------------------------------')
# Method items
print(contacts.items())

print('-----------------------------------------------------------------------------')
# Method keys
print(contacts.keys())

print('-----------------------------------------------------------------------------')
# Method values
print(contacts.values())

print('-----------------------------------------------------------------------------')
# Method pop
print(person2)
person2.pop('age')
print(person2)
person2.pop('age', {})
print(person2)

print('-----------------------------------------------------------------------------')
# Method popitem
person2.popitem()
print(person2)
person2.popitem()
print(person2)

print('-----------------------------------------------------------------------------')
# Method setdefault
person2 = {}
person2.setdefault('firstname', 'Janet')
print(person2)
person2.setdefault('lastname', 'Jackson')
print(person2)
person2.setdefault('gender', 'female')
print(person2)
person2.setdefault('age', 20)
print(person2)

print('-----------------------------------------------------------------------------')
# Method update
person2.update({'firstname': 'Michael', 'gender': 'male', 'age': 53})
print(person2)

print('-----------------------------------------------------------------------------')
# Method in
print('firstname' in person2)
print('gender' in person2)
print('email' in person2)

print('-----------------------------------------------------------------------------')
# Method del
del person2['age']
print(person2)