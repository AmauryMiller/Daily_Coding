# Ejercicios

def city_country(city, country):
    """Formateo de función"""
    print(f"{city.title()}, {country.title()}")

city_country('cdmx', 'mexico')

def make_album(artist_name,album_title,number_songs = None):
     """Return a dictionary information about a person"""
     if number_songs:
        album = {'artist_name': artist_name, 'album_title': album_title, 'number_songs': number_songs}
        print(album)
     else:
        album = {'artist_name': artist_name, 'album_title': album_title}   
        print(album) 

make_album(artist_name = 'Frank Sinatra', album_title = 'My Way')
make_album(artist_name = 'El Simbolo', album_title = 'De reversa', number_songs=13) 

#Con petición de usuario y loop
def make_album(artist_name,album_title,number_songs = None):
     """Return a dictionary information about a person"""
     
     album = {'artist_name': art_name, 'album_title': alb_title, 'number_songs': numb_songs}
     return album

while True:
    print("\nEscribe el nombre del artista")
    print("(pon 'q' para salir")

    art_name = input("Nombre del artista: ")
    if art_name == 'q':
        break
    
    alb_title = input("Nombre del Album: ")
    if alb_title == 'q':
        break
    
    numb_songs =input("Numero de canciones")
    if num_songs == 'q':
        break
    
    new_album = make_album(art_name, alb_title, numb_songs)
    print(f"{new_album}")


# Passing a list

def greet_users(names):
    """Print a simple greeting to each user in the list"""
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)

usernames =['hannah', 'ty', 'margot']
greet_users(usernames)
         

# Modificando una lista en una función
# Empezamos con diseños que necesitan imprimirse.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simula imprimir cada diseño, hasta que ninguno quede.
# Mueve cada diseño a completed_models despues de imprimir.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Imprimiendo modelo: {current_design}")
    completed_models.append(current_design)

# Muestra todos los modelos completos.
print("\nLos siguientes modelos han sido impresos: ")
for completed_model in completed_models:
    print(completed_model)

# Con funciones
def print_models(unprinted_designs, completed_models):
    """
    Simula imprimir cada diseño, hasta que no quede ninguno.
    Mueve cada diseño a completed_models despues de imprimir.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Imprimiendo modelo: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Muestra todos los modelos que se imprimen"""
    print("\nLos siguientes modelos han sido impresos: ")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

#print_models(unprinted_designs[:],completed_models) --ponerlo de esta forma crea una copia
# de unprinted_designs sin alterar la lista original
print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)



