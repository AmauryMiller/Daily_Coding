def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello! {username.title()}")

greet_user('amaury')

def describe_pet(pet_name, animal_type = 'perrito'):
    """Display information about the pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.'")

describe_pet('alpha')
describe_pet(pet_name = 'harry', animal_type = 'hamster')

def get_formatted_name(first_name, last_name , middle_name = ''):
    """Regresa el nombre formateado"""
   
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
        return full_name.title()
    else:
        full_name = f"{first_name} {last_name}"
        return full_name.title()

musician = get_formatted_name(first_name = 'erasmo' , last_name = 'catarino' , middle_name = 'mariposa')
print(musician)

musician = get_formatted_name(first_name = 'erasmo' , last_name = 'catarino')
print(musician)

# Valor none se toma por defecto como falso
def build_person(first_name,last_name, age=None):
    """Return a dictionary information about a person"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
        return person

musician = build_person ('jimi', 'hendrix' , age=27)
print (musician)


# Función con un while
def get_formatted_name2(first_name, last_name):
    """Regresa el nombre formateado"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nDime tu nombre:")
    print("Pon 'q' para salir")

    f_name = input("First Name: ")
    if f_name == 'q':
        break

    l_name = input("Last Name: ")
    if l_name == 'q':
        break

    formatted_name2 = get_formatted_name2(f_name, l_name)
    print(f"\nHola {formatted_name2}")