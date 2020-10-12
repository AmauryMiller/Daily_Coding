# Ejercicio

pets = {
    'firulais': {
        'owner': 'albert',
        'type': 'perrito',
        },
    'fishi': {
        'owner': 'aquaman',
       'type': 'pescadito',
        }
    }

for petname, pet_info in pets.items():
    print(f"\nPet name: {petname}")
    print(f"\tOwner name: {pet_info['owner'].title()}")
    print(f"\tType: {pet_info['type'].title()}")