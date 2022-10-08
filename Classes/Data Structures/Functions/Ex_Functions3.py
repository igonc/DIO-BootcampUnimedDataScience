def addcar(model, brand, color, year, license):
    print(f'Car successfully inserted: {model}/{brand}/{color}/{year}/{license}')

addcar('Palio', 'Fiat', 'red', 2009, 'ABC-1234')
addcar(model='Corsa', brand='Fiat', color='green', year=2011, license='JKL-2020')
addcar(year=2011, brand='Fiat', color='green', license='JKL-2020', model='Corsa')
addcar(**{'model': 'Corsa', 'brand': 'Fiat', 'color': 'green', 'year': 2011, 'license': 'JKL-2020'})
addcar(**{'year': 2011, 'brand': 'Fiat', 'color': 'green', 'license': 'JKL-2020', 'model': 'Corsa'})
