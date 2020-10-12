prompt = "Dime algo y te lo repito:"
prompt += "\nEnter 'quit' to end the program"
message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)

name = input("Escribe tu nombre")
print(f"Hola Pequeño {name.title()}")

height = input("How tall are you?")
height = int(height)

if height >= 48:
    print("\nEres lo sufucientemente alto!")
else:
    print("\nEstas bajito!")

number = input("Escribe un numero y te dire si es non o par")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} es par.")
else:
    print(f"\nThe number {number} es non.")

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number +=1


prompt = "Dime algo y te lo repito:"
prompt += "\nEnter 'quit' to end the program"

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)


prompt = "\nAnota una ciudad que hayas visitado"
prompt += "\n(Pon 'quit' cuando termines)"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"Me gusta ir a {city.title()}!")

current_number = 0
while current_number < 10:
    current_number +=1
    if current_number % 2 == 0:
        continue

    print(current_number)

# Ejercicio

prompt = input("Inserte su edad para consultar tarifa")

age = int(prompt)

if age < 3:
    print("Gratis")
elif age >= 3 and age < 12:
    print("10 pesitos")
else:
    print("15 pesitos general")

# While loop en listas y diccionarios
# Empieza con lista de usuarios que deben ser verificados
# Una lista vacia para resguardar usuarios confirmados

unconfirmed_users = ['alice','brian','candance']
confirmed_users = []

# Verifica cada usuario hasta que no haya mas no confirmados
# Mueve cada usuario a la lista de usuarios confirmados
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verificando usuario: {current_user.title()}")
    confirmed_users.append(current_user)

# Muestra todos los usuarios confirmados

print("\n Los siguientes usuarios han sido confirmados:")

for confirmed_user in confirmed_users:
    print(confirmed_user.title())


pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets:
     pets.remove('cat')

print(pets)   


responses = {}

#Bandera de activo
polling_active = True

while polling_active:
    #Pide persona y respuesta
    name = input("\n¿Cual es tu nombre?")
    response = input("¿Que montaña le gustaria escalar algun dia?")

    #Guarda respuesta en el diccionario
    responses[name] = response

    #Petición de usuario adicional

    repeat = input("¿Permitiras a otra persona responder? (yes/no)")
    if repeat == 'no':
        polling_active = False

# Polling is complete , show results
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")


#Ejercicios

sandwich_orders = ['atun','pastrami','puerco','lechuga','pastrami','huevo','pastrami']
finished_sandwiches = []

# No pastrami
print("Deli run out of pastrami =(")
while 'pastrami' in sandwich_orders:
     sandwich_orders.remove('pastrami')


while sandwich_orders:
    finished_sandwiches = sandwich_orders.pop()
    print(f"i made your {finished_sandwiches} sandwich!")
    