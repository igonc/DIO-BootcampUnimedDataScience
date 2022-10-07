# Dictionaries are denoted with curly brackets
# They are comprised by keys and values
# Each value can be accessed through a key using square brackets
# The keys have to be immutable and unique

dic1 = {'maçã': 20, 'banana': 15, 'laranja': 5, 'abacaxi': 10}
print(dic1)
print(dic1.keys())
print(dic1.values())
print(dic1['maçã'])
dic1['banana'] = 0 # Replacing a value
print(dic1)
dic1.setdefault('limão', -5) # Adding a new entry
dic1['peach'] = 45 # Adding a new entry
print(dic1)
del(dic1['abacaxi']) # Removing an element
print(dic1)
print('maçã' in dic1)
