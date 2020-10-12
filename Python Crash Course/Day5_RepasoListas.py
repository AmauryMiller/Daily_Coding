#Ejercicio de Uso de Listas

#users = ['amaury','admin','martha','alpha','kokoa']
users = []

if users:
    for user in users:
        if user.upper() == 'ADMIN':
            print(f"Hola dios {user.title()}! ¿Quieres un reporte de estatus?")
        else:
            print(f"Hola mortal {user.title()}")
else:
    print("Necesitamos Banda!")

#Ejercicio con cambio de listas
current_users = ['amaury','admin','martha','alpha','kokoa']
new_users = ['oscar','ADMIN','tito','alphA','tita']
nuevos_list = []

for new_user in new_users:
     nuevos_list.append(new_user.lower())

for nuevo_list in nuevos_list:
     if nuevo_list in current_users:
        print(f"El nombre {nuevo_list.upper()} ya existe, elige otro!")
     else:
        print(f"El nombre {nuevo_list} esta disponible")

#Numero Ordinales

numbers= list(range(1,11))

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")


