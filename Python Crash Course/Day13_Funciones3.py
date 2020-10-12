def show_messages():
    send_messages = ['Hola', 'Aloha', 'Bonjorno', 'Aios', 'Bye', 'Arrivederchi']
    sent_messages = []
    new_list = send_messages [:]


    while new_list:
        message = new_list.pop()
        sent_messages.append(message)
        print(f"{message}, Amaury!")

    print(send_messages)
    print(sent_messages)
        
     
show_messages()

# REcibe n numero de argumentos

def make_pizza(size, *toppings):
    """Print the list of toppings that have been requested."""
    print(f"\nMaking a {size} inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# **user_info (pair) Crea diccionarios vacios

def build_profile(first, last, **user_info):
    """Build a dictionary continiendo todo lo que sabemos del usuario"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location = 'princeton',
                             field = 'physics')

print(user_profile)

