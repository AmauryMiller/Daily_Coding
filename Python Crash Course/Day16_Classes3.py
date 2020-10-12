# Ejercicios

class Restaurant:
    """Modelando un restaurante"""

    def __init__(self,restaurant_name,cuisine_type):
        """Inicializa el nombre del restaurante y el tipo de cocina"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """Describe e imprime las caracteristicas del restaurante"""
        print(f"Bienvenido al restaurante {self.restaurant_name}",
            f"nos especializamos en cocina {self.cuisine_type}")
    
    def open(self):
        """Simula la apertura del restaurante"""
        print(f"el Restaurante {self.restaurant_name} esta abierto!")


class IceCreamStand(Restaurant):
    """Anexando flavors"""

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an Ice cream stand
        """
        super().__init__(restaurant_name,cuisine_type)
        
                

    def flavors(self,sabores):
            self.flavors = sabores
            print(f"El sabor elegido es: {self.flavors}")
            


my_icecream = IceCreamStand('La Michoacana','Heladitos')
my_icecream.describe_restaurant()
my_icecream.flavors('Chico Zapote')

##

