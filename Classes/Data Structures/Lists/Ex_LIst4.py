# Method Append

employee = []

employee.append('Smith')
employee.append('John')
employee.append(42)
employee.append('Web Dev')
print(employee)

# Method Clear

employee.clear()
print(employee)

# Method Copy

fruits = ['strawberry', 'blackberry', 'raspberry', 'blueberry']
berries = fruits.copy()
fruits.extend(['apple', 'orange', 'peach', 'mango'])
print(fruits)
print(berries)

# Method Count

colors = ['red', 'orange', 'green', 'yellow', 'blue', 'orange', 'gray', 'pink', 'purple', 'orange', 'green']
print('The orange color appears: ', colors.count('orange'), 'times')

# Method Extend

code_languages = ['python', 'java', 'javascript', 'c']
print(code_languages)
code_languages.extend(['python', 'c++', 'c#'])
print(code_languages)

# Method Index

print(code_languages.index('python'))

# Method Pop 

print(code_languages.pop())
print(code_languages.pop())
print(code_languages.pop())
print(code_languages)

# Method Reverse

code_languages.reverse()
print(code_languages)

name = list('Rodrigo')
print(name)
name.reverse()
print(name)

# Method Sort

code_languages.extend(['python', 'c++', 'c#'])
print(code_languages)
code_languages.sort()
print(code_languages)
code_languages.sort(reverse=True)
print(code_languages)
code_languages.sort(key=lambda x: len(x))
print(code_languages)
code_languages.sort(key=lambda x: len(x), reverse=True)
print(code_languages)

# Function Len 
print(code_languages)
print(len(code_languages))
code_languages.extend(['r', 'pascal'])
print(code_languages)
print(len(code_languages))

# Function Sorted
print(sorted(code_languages))
print(sorted(code_languages, key=lambda x: len(x), reverse=True))