rivers = {
        'nile': 'egypt',
        'yangtze': 'china',
        'amazon': 'brazil'
}

for river, country in rivers.items():
    print(f"The {river.title()} river is located in {country.title()}")

print("\nThe following rivers are within dictionary")
for river in rivers.keys():
    print(river.title())
    
print("\nThe following countries are within dictionary")
for country in rivers.values():
    print(country.title())
