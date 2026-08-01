cities = {
    'Tokyo': {
        'Country': 'Japan',
        'Population': '14 Million',
        'Fact': 'Biggest Metropolitan area worldwide',
    },
    'Paris': {
        'Country': 'France',
        'Population': '2.1 Million',
        'Fact': 'Known as the City Of Light'
    },
    'Cairo': {
        'Country': 'Egypt',
        'Population': '10 Million',
        'Fact': 'Sits next to Ancient Giza Pyramids',
    },
}

for citys, city_info in cities.items():
    print(f"\n{citys}")
    print(f"\tCountry: {city_info['Country']}")
    print(f"\tPopulation: {city_info['Population']}")
    print(f"\tFact: {city_info['Fact']}")
