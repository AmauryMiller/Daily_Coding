#Ejercicio Listas
items= ['alpha', 'beta' , 'gamma', 'delta' , 'omicron']

print("The first three items in my list are:")
print(items[:3])
print("The middle items in my list are:")
print(items [2:4])
print("The last three items in my list are:")
print(items[-3:])

my_pizzas = ['peppeponi','quesito','callejera']
friend_pizzas= my_pizzas[:]
my_pizzas.append('especial')
friend_pizzas.append('parisina')

for my_pizza in my_pizzas:
    print(f"My favorite pizza is {my_pizza}")


for friend_pizza in friend_pizzas:
    print(f"His favorite pizza is {friend_pizza}")

#Tuplas : Una lista inmutable

dimensions= (200,50)
print(dimensions[0])
print(dimensions[1])

print("Original Dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions= (400,100)
print("\nModofied Dimensions:")
for dimension in dimensions:
    print(dimension)

#Ejercicio Tuplas

comidas=('kekas','chanwich','trufa','huevito','horchata')

print("El menu estandar es:")
for comida in comidas:
    print (comida)

comidas=('kekas','pan frances','trufa','atun','horchata')

print("\nEl menu nuevo es:")
for comida in comidas:
    print (comida)



