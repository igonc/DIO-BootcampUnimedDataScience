# Lists are data structures
# Lists are ordered sequences written as comma-separated elements within square brackets
# They can nest strings, integers, floats and other lists
# Each element can be accessed through an index
# We can concatenate or combine lists by adding them
# Lists are mutable structures

list1 = ['dog', 'cat', 'rat', 'habbit', 'gold fish', 2, 6, True]
print(list1)
print(len(list1))
print(list1.count('dog'))
print(list1[0:5])
list1[4] = 'spider'
print(list1)
list1.remove('spider')
print(list1)
list1.append('snake')
print(list1)
list1.extend(['turtle', 'bat'])
print(list1)
print(list1.count('turtle'))
list1.append(['lion', 'tiger'])
print(list1)

list2 = ['monkey', 'lizard']
print(list2)
list3 = list1 + list2
print(list3)

list4 = list2[:] # cloning a list 
list2[1] = 'cricket'
print(list2)
print(list4)
list3 = list1 + list2
print(list3)
del(list3[0])
print(list3)
print('cricket' in list3)
print('gold fish'.split())

