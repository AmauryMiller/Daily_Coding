# Ejercicios

persons = {
    'first_name': 'Amaury',
    'last_name': 'Miller',
    'age': 33,
    'city': 'méxico',
    }

print(f"Your first name is {persons['first_name']} and your last name is {persons['last_name']}")
print(f"You age is {persons['age']} and you live in {persons['city'].title()}.")

friend_numbers = {
    'Amaury': 18,
    'Martha': 17,
    'Alpha': 15,
    'Tito': 1,
    'Pepe': 2,
    }

print(f"Your favorite number Amaury is {friend_numbers['Amaury']}")
print(f"Your favorite number Martha is {friend_numbers['Martha']}")
print(f"Your favorite number Alpha is {friend_numbers['Alpha']}")

#Ciclos en diccinarios

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

for name in favorite_languages.keys():
    print(name.title())


friends = ['phil','sarah']

for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, i see you love {language}!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# Acomodar el diccionario previo a trabajarlo

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

#Usar Set para quitar duplicados
print("The following languages have been mentioned:")

for language in  set(favorite_languages.values()):
    print(language.title())

#Ejemplo

aliens = []
# Hacer 30 aliens

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)

# Len cuenta registros del diccionario
print(f"Total number of aliens: {len(aliens)}")

#Una Lista en in directorio

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms','extra cheese'],
    }

print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

#Otro Ejemplo
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby','go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")
    else:
        print(f"\n{name.title()}'s favorite language is:")
        for language in languages:
            print(f"\t{language.title()}")


# Un diccionario en un diccionario

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },

    'mcurie' : {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris', 
        },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
