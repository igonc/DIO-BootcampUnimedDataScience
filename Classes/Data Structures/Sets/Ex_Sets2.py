cars = {'Ferrari', 'Lamborghini', 'Ferrari', 'Jaguar', 'Porche', 'Ferrari', 'Porche'}
print(cars)
print(type(cars))

for car in cars:
    print(car)

for indice, car in enumerate(cars):
    print(f'{indice}: {car}')