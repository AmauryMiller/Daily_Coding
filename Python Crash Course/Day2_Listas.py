#Una lista se encierra en corchetes, donde el primer registro siempre es 0
bicycles =['Shimano','Bimex','Magistroni','Apache']
print (bicycles)
print (bicycles[0].upper())
# -1 muestra el ultimo elemento de la lista
print (bicycles[-1].upper())
message= f"Mi primera bicicleta fue una {bicycles[3].upper()}"
print (message)

motocicletas= ['honda','yamaha','suzuki']
print(motocicletas)

motocicletas.append('ducati')
#motocicletas[0]= 'ducati'
print (motocicletas)

#Agregando elementos a una lista vacia
motocicletas2=[]
motocicletas2.append('honda')
motocicletas2.append('yamaha')
motocicletas2.append('suzuki')
print(motocicletas2)

#La inserción manda el dato a una posición y recorre el resto
motocicletas2.insert(0,'ducati')
print (motocicletas2)
#borrado permanente
del motocicletas2[0]
print (motocicletas2)

#borra el ultimo item de la lista pero lo resguarda
popped_motocicletas2= motocicletas2.pop()
print(motocicletas2)
print(popped_motocicletas2)
#pop resguarda el item que se remueve de la lista
motocicletas3= ['honda','yamaha','suzuki']
last_owned=motocicletas3.pop()
print(f"Mi ultima motocicleta que tuve fue una {last_owned}")
first_owned=motocicletas3.pop(0)
print(f"Mi primera motocicleta que tuve fue una {first_owned}")

#remove quita la primera ocurrencia del valor, si hay más es preciso hacer un ciclo
motocicletas4= ['honda','yamaha','suzuki','ducati']
motocicletas4.remove('ducati')
print(motocicletas4)

too_expensive='yamaha'
motocicletas4.remove(too_expensive)
print(motocicletas4)
print(f"\nA {too_expensive} is too expensive for me.")

#Ejercicio
people_invite= []
people_invite.append('Yamcha')
people_invite.append('Goku')
people_invite.append('Kaio Sama')
print(people_invite)
message=f"Ven a mi casa por unas cheves {people_invite[0]}"
print(message)
#Goku se fue a entrenar y no vendra
people_invite[1]= 'Luffy'
message=f"Ven a mi casa por unas cheves {people_invite[1]}"
print(message)
print("Se abren 3 lugares más")
people_invite.insert(0,'Tanjiro')
people_invite.insert(3,'Deku')
people_invite.append('Saibaiman')
message2=f"Bienvenidos a la fiesta {people_invite[0]} , {people_invite[3]} y {people_invite[-1]} "
print(message2)

print("nos quedo mal el de la mesa y tendre que desinvitar gente")
desenvitado=people_invite.pop()
print(f"Amigo {desenvitado} tu te vas!")
desenvitado=people_invite.pop()
print(f"Amigo {desenvitado} tu te vas!")
desenvitado=people_invite.pop()
print(f"Amigo {desenvitado} tu te vas!")
desenvitado=people_invite.pop()
print(f"Amigo {desenvitado} tu te vas!")
print(f"{people_invite[0]} y {people_invite[-1]} se salvaron! Bienvenidos!")
print("La fiesta se acabo")
del  people_invite [0] , people_invite [-1]
print(people_invite)

#Ordenamiento de Listas

#Sort acomoda y mueve la estructura inicial permanentemente
cars= ['bmw','audi','toyota','subaru']
cars.sort(reverse=True)
print(cars)

#Sorted ordena para visualización pero mantiene el orden inicial
cars2= ['bmw','audi','toyota','subaru']

print("Here is the original list:")
print(cars2)
print("\nHere is the sorted list:")
print(sorted(cars2,reverse=True))
print("\nHere is the original list again:")
print(cars2)
#Reverse voltea solamente la lista sin ordenarla permanentemente
cars2.reverse()
print(cars2)
#Largo de una lista
print(len(cars2))

