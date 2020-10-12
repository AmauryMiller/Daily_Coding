# Condicipon IF
cars=['audi','bmw','subaru','toyota']

for car in cars:
     if car == 'bmw':
         print(car.upper())
     else:
         print(car.title())

#Desigualdad
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies")

answer = 17

if answer != 42:
    print("That´s not the correct answer. Please try again!")

#Uso de NOT IN
banned_users =['andrew','carolina','david']
user= 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Estas chavo!")

#Multiples IFS
age = 1

if age < 4:
    print("Entras gratis!")
elif age < 18:
    print("Son 25 Morlacos")
else:
    print("Son 40 Morlacos")

#Ejercicio

alien = "red"

if alien == "green":
    points = 5
elif alien == "yellow":
    points = 10
elif alien == "red":
    points = 15

print(f"You hit the {alien} alien, You Won {points} points!")

number = 17

if number < 2:
    age = "baby"
elif (number >= 2) and (number < 4):
    age = "toddler"
elif (number >= 4) and (number < 13):
    age = "kid"
elif (number >= 13) and (number < 20):
    age = "teenager"
elif (number >= 20) and (number < 65):
    age = "adult"
else:
    age = "elder"

print(f"The person is a {age.upper()}")

#IF dentro del FOR

requested_toppings = ['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print(f"We don´t have {requested_topping}.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

#Verificacipon si la lista esta vacia o no
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
         print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("¿Estas seguro que quieres masita sola?")

# Listas multiples

avaliable_toppings = ['mushrooms','olives','green peppers','pepperoni',
                      'pineapple','extra cheese']

requested_toppings = ['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in avaliable_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don´t have {requested_topping}")

print("You´re pizza is ready!")






