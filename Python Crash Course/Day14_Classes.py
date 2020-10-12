# Init corre automaticamente cuando se crea una instancia

class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
        
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
my_dog.sit()
my_dog.roll_over()

print(f"My dog's name is {my_dog.name}")
print(f"My dog's age is {my_dog.age} years old.")

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

my_restaurant = Restaurant('Patitas y Mollejas', 'Callejera')

my_restaurant.describe_restaurant()
my_restaurant.open()

class Users:
    """Registo de usuarios"""

    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
    
    def describe_user(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Country: {self.country}")
    
    def greet_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        print(f"\nHola {full_name.title()}")

user1= Users('amaury', 'miller', 33, 'México')
user1.describe_user()
user1.greet_user()

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Inicializa atribuos de descripción carro"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 50
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Imprime el kilometraje del auto"""
        print(f"This car has {self.odometer_reading} miles on it")
    
    def update_odometer(self, mileage):
        """Set the odometer to a given value and reject the value if the odometer rolls back"""

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can roll back the odometer!")
    

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(1)
my_new_car.read_odometer()
        