numbers = list(range(21))
print(numbers)
numbers_even = []
numbers_odd = []

for number in numbers:
    if number % 2 == 0:
        numbers_even.append(number)
    else: numbers_odd.append(number)

print(numbers_even)
print(numbers_odd)

print()

num_even = [number for number in numbers if number % 2 == 0]
num_odd = [number for number in numbers if number % 2 != 0]
print(num_even)
print(num_odd)

square = []
for number in numbers:
    square.append(number**2)
print(square)

cubic = [number**3 for number in numbers]
print(cubic)