filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I love finding meaning in large datasets. \n.")
    file_object.write("I love creating apps that can run in a browser. \n.")

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)


def count_words(filename):
    """Count the approximate number of words in a file"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()

    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")
    

filename= ' alice.txt'
count_words(filename)   

# Guardo info
import json

username = input("What´s your name?")

filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}!")

# invoco info
import json

filename = 'username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Bienvenido, {username}!")

# Combinado

# Load the username, if it has benn stored previously.
# Otherwise, prompt for the username and sotre it.
import json

filename = 'username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name?")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Bienvenido, {username}!")

# En funciones

import json            

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt FOR A NEW USERNAME"""
    username = input("What is your name?")
    filename = 'username.json'
    with open(filename, 'w') as f:
            json.dump(username, f)
    return username


def greet_user():
    """Greet the user by name"""
    username = get_stored_username()
    filename = 'username.json'
    if username:
        print(f"Bienvenido, {username}!")
    else:
        username = get_new_username()        
        print(f"We'll remember you when you come back, {username}!")

greet_user()
