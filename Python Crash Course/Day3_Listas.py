#Uso de FOR para desplazarnos en listas
magicians = ['alice','david','carolina']
for magician in magicians:
    print (f'{magician.title()}, that was a great trick!')
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")

#Ejercicio
pizzas = ['peppeponi','quesito','callejera']
for pizza in pizzas:
    print(f"I like {pizza.title()} pizza!")

print(f"I like {pizzas[0].title()} and {pizzas[1].title()} pizza, but the most i want always is {pizzas[-1].title()} pizza")
print("I Like Pizzitas!")

animalitos= ['perrito','fungus','termita']
for animalito in animalitos:
    print(f"{animalito.upper()} es una gran mascota")
    
print("Vivan los animalejos")

#Rangos

for value in range(1,6):
    print (value)
# Comando LIST
numbers= list(range(1,6))
print(numbers)

even_numbers= list(range(2,11,2))
print(even_numbers)

squares= []
for value in range(1,11):
    square= value**2
    squares.append(square)

print(squares)

#Otra forma
squares= []
for value in range(1,11):
    squares.append(value**2)
print(squares)

digits = [1,2,3,4,5,6,7,8,9,0]
min(digits)
max(digits)
sum(digits)

#Forma PrO con List Comprehension
squares= [value**2 for value in range(1,11)]
print (squares)

#Ejercicios
numeros= list(range(1,1_000_001) )
min(numeros)
max(numeros)
sum(numeros)

nones_numeros= list(range(1,20,2))
print (nones_numeros)

multiplostres= [value*3 for value in range(1,11)]
print (multiplostres)

cubos= [value**3 for value in range(1,11)]
print (cubos)

#Trabajar con slices
players= ['charles','martina','michael','florence','eli']
print(players[1:4])
print(players[:4])
#Los ultimos 3
print(players[-3:])

players2= ['charles','martina','michael','florence','eli']
print("Here are the first three players on my team:")
for player in players2[:3]:
    print(player.title())

#Copiar una lista completa
my_foods = ['pizza','falafel','carrot cake']
#Es importante mantener la copia del slice pues al no tenerlo se apunta
#una lista a la otra y es como si fuera la misma lista
friend_foods = my_foods[:]   

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend´s favorite foods are:")
print(friend_foods)