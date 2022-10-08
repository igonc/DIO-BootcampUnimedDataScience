cars = ('Ferrari', 'Lamborghini', 'Porche')
print(type(cars))
for car in cars:
    print(car)

for indice, car in enumerate(cars):
    print(f'{indice}: {car}')

