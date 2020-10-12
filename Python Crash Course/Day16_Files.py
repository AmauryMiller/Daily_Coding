with open('pi_digits.txt') as file_object:
    contents = file_object.read()

print(contents.rstrip())

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    

pi_string = ''
for line in lines:
        pi_string += line.strip()


birthday = input("Enter your birthday, in the form mmddyy:")
if birthday in pi_string:
    print(f"Your birthday appears in the first million digits of pi!")
else:
    print("Gracias por participar!")

