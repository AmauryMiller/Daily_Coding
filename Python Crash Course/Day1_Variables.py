# Dia 1 de 366 daily coding
print("Hello python world!")

message= "Hello python world!"
print(message)

message= "Hello python Crash Course world!"
print(message)

#Manipulando formato de cadenas
name= "amaury miller"
print(name.title())
print(name.upper())
print(name.lower())

#Formatos
first_name= "amaury"
last_name="miller"
fullname= f"{first_name} {last_name}"
print(fullname)
print(f"Hola Guapo!, {fullname.title()}")
message=f"Hola Guapo!, {fullname.upper()} quieres aprender algo de Python hoy?"
print(message)
#Tabulaciones y nuevas lineas
print("Primera Linea\nSegunda Linea\n\tTercera Linea tabulada")

#Quitar espacios en blanco
favorite_language= " python "
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())

#Uso de Comillas
message3= "one of python's strenghts is its diverse community."
print(message3)

#Escribir una frase
author="Albert Einstein"
quote="A person who never made a mistake never tried anything new"
print(f"{author} once said, {quote}")

#Trabajando con Numeros
print(2+3)
#Las potencias se marcan con **
print(2**3)
#Cualquier operación con flotante te devuelve flotante
print(2.5**2)
print(4/2)
#Los guiones bajos sirven para separar cantidades pero no afectan al numero
universe_age=14_000_000
print(universe_age)
#Asignación Multiple
x,y,z = 0,0,0
#Cuando se escriben constantes es bueno documentarlas en Mayuscula
MAX_CONNECTIONS=5000

favorite_number=18
print(f"My favorite number is {favorite_number}")
#Zen to python
import this
