def sum_of_numbers(numbers):
    return sum(numbers)

def predecessor_and_successor(number):
    predecessor = number - 1
    successor = number + 1
    return predecessor, successor

print(sum_of_numbers([10, 20]))
print(predecessor_and_successor(24))