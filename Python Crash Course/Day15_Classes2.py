# Ejercicio 1

class Restaurant:
    """Modelando un restaurante"""

    def __init__(self,restaurant_name,cuisine_type):
        """Inicializa el nombre del restaurante y el tipo de cocina"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 69
    
    def describe_restaurant(self):
        """Describe e imprime las caracteristicas del restaurante"""
        print(f"Bienvenido al restaurante {self.restaurant_name}",
            f"nos especializamos en cocina {self.cuisine_type}",
            f"Hemos atendido {self.number_served}")
    
    def open(self):
        """Simula la apertura del restaurante"""
        print(f"el Restaurante {self.restaurant_name} esta abierto!")
    
    def set_number_served(self,served):
        self.number_served = served
        print(f"Has servido {self.number_served} platos")
    
    def increment_number_served(self,increment):
        self.number_served = self.number_served+increment
        print(f"Has servido {self.number_served} platos")


my_restaurant = Restaurant('Patitas y Mollejas', 'Callejera')

my_restaurant.describe_restaurant()
my_restaurant.set_number_served(101)
my_restaurant.increment_number_served(5)

# Ejercicio 2

class Users:
    """Registo de usuarios"""

    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.login_attempts = 99
        
    
    def describe_user(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Country: {self.country}")
        print(f"Sesiones Totales: {self.login_attempts}")
    
    def greet_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        print(f"\nHola {full_name.title()}")
    
    def increment_logging_attempts(self):
        self.login_attempts= self.login_attempts + 1
        print(f"Sesión numero: {self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0

user1= Users('amaury', 'miller', 33, 'México')
user1.greet_user()
user1.increment_logging_attempts()
user1.describe_user()
user1.reset_login_attempts()
user1.describe_user()


class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Inicializa atribuos de descripción carro"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
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
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery:
    """A simple attempt to model a battery for an electric car"""

    def __init__(self, battery_size = 75):
        """Initialize battery's attributes"""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size} -Kwh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        
        print(f"This car can go about {range} miles on a full charge")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car
        """
        super().__init__(make, model, year)
        self.battery = Battery()
    
    
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()