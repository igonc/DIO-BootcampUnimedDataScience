print('----------------------------------------------------------')
# MethoU2 Union
A = {-5, -4, -3, -2, -1, 0, 1, 2}
print('A = ', A)
B = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print('B = ', B)

U1 = A.union(B)
print('U1 = A + B = ', U1)
U2 = B.union(A)
print('U2 = A + B = ', U2)

print('----------------------------------------------------------')
# Method Intersection
I1 = A.intersection(B)
print('I1 = ', I1)
I2 = B.intersection(A)
print('I1 = ', I2)

print('----------------------------------------------------------')
# Method Difference
D1 = A.difference(B)
print('D1 = A - B =', D1)
D2 = B.difference(A)
print('D2 = B - A = ', D2)

print('----------------------------------------------------------')
# Method Symetric_difference
S = A.symmetric_difference(B)
print('S = ', S)

print('----------------------------------------------------------')
# Method Issubset
print(A.issubset(B))
print(B.issubset(A))
print(I1.issubset(A))
print(I2.issubset(B))

print('----------------------------------------------------------')
# Method Issuperset
print(A.issuperset(B))
print(B.issuperset(A))
print(I1.issuperset(A))
print(I2.issuperset(B))
print(A.issuperset(I1))
print(B.issuperset(I2))

print('----------------------------------------------------------')
# Method isdisjoint
print(A.isdisjoint(B))
print(D1.isdisjoint(A))
print(D1.isdisjoint(B))

print('----------------------------------------------------------')
# Method add
print('B = ', B)
B.add(9)
B.add(10)
print('B = ', B)

print('----------------------------------------------------------')
# Method copy
b = B.copy()
print('B = ', B)
print('b = ', b)

print('----------------------------------------------------------')
# Method clear
B.clear()
print('B = ', B)
print('b = ', b)

print('----------------------------------------------------------')
# Method discard
b.discard(10)
print('b = ', b)

print('----------------------------------------------------------')
# Method pop
b.pop()
print('b = ', b)
b.pop()
print('b = ', b)

print('----------------------------------------------------------')
# Method remove
b.remove(9)
print('b = ', b)

print('----------------------------------------------------------')
# Method len
print(len(b))

print('----------------------------------------------------------')
# Method in
print('3 in b? ', 3 in b)
print('-3 in b? ', -3 in b)