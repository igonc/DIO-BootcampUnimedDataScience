# Tuples are data structures
# Tuples are ordered sequences written as comma-separated elements within square brackets
# They can nest strings, integers, floats and other Tuples
# Each element can be accessed through an index
# We can concatenate or combine Tuples by adding them
# Tuples are immutable structures

tuple1 = ('banana', 'maçã', 10, 20, True, False, 3.1415)
print(tuple1)
print(len(tuple1))
print(type(tuple1))
print(tuple1[0])
print(tuple1[:2])
print(tuple1[2:])

tuple2 = (1000, -6, 0, 100, 1.2, -50)
print(tuple2)
tuple2sorted = sorted(tuple2)
print(tuple2sorted)

tuple3 = tuple1 + tuple2
print(tuple1)
print(tuple2)
print(tuple3)

# Tuples nesting
tuple4 = (1, 2, ('pop', 'rock', 'hiphop'))
print(tuple4)
print(tuple4[2])
print(tuple4[2][1])
print('rock' in tuple4)
print('hiphop' in tuple4[2])
