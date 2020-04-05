import emojis as em
import converters as con
from ecommerce import shipping
import random
from pathlib import Path

'''birth_year = input("Birth year: ")
age = 2020 - int(birth_year)
print(age)

#######################################
#Strings

title = "Jennifer"
another = title[1:-1]

print(another)

#formatted strings
first = "John"
last = "Smith"
message = first + " [" + last + "] is a coder"  #string concatination
msg = f"{first} [{last}] is a coder"            #formatted strings - prefix with f and use {}
print(message)
print(msg)

#String Methods
course = "Python for Beginners"
print(len(course))                              #len() can count numbers in a list also

print(course.upper())
print(course.replace("r", "ttt"))
print("Python" in course)                       #Boolean expression


################################
#Arithmetic Expressions
print(10 ** 2)                                  #power of
print(10 // 4)                                  #divide and print int
#Augmented assigned operator
x = 10
x -= 3
print(x)

#operator precedence given in Python

#Match functions
import math
x = -2.5000001
y = math.sqrt(144)
print(abs(x), y)

#Conditions
is_hot = False
is_cold = False
if is_hot:
    print("It's a hot day! ")
    print("Dring a lot of water! ")
elif is_cold:
    print("It's a cold day! ")
else:
    print("It  a lovely day! ")
print("Enjoy your day! ")

price = 1000000
good_credit = False
if good_credit:
    put_down = price * 0.1
    print(put_down)
else:
    put_down = price * 0.2
    print(f"Down payment is €{put_down}." )

#Logical operators
price = 22
size = 42

if price > 120:
    print(f"The price is {price}. That is low!.")
elif price <=33 and size >=40:
    print(f"This is awesome!! The shoes are size {size} for just €{price}!.")


name = "Michael Knight is the one and only king of the car good"
if len(name) < 3:
    print("The name must be at least 3 letters long! ")
elif len(name) > 50:
    print("Name can only consist of maximum 50 letters." )
else:
    print(f"Looks good {name}! ")

#Small programm conversion pounds to kilogram
weight = int(input("Please insert your weight. "))
type_of_weight = input("(L)bs or (K)g: ")
if type_of_weight.upper() == "L":
    print(f"You are {weight*2.2} pounds. ")
elif type_of_weight.upper() == "K":
    print(f"You are {weight/2.2} kilogram. ")

#While loop
i = 1
while i <= 5:
    print('*' * i)
    i += 1


secret_number = 4
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("Right guess! ")
        break
    elif guess_count == guess_limit:
        print("You guessed incorrectly! ")

help = ""
status = ""
while True:
    help = input().upper()
    if help == "START":
        if status == "START":
            print(f"We are already on {status}. ")
        else:
            print("Car started...Ready to go! ")
            status = "START"
    elif help == "STOP":
        if status == "STOP":
            print(f"We are already on {status}. ")
        else:
            print("Car stopped. ")
            status = "STOP"
    elif help == "QUIT":
        break
    elif help == "HELP":
        print("""
start - to start the car 
stop - to stop the car
quit - to exit """)
    else:
        print("I could not understand your command. ")

for item in range(5,11, 2):
    print(item)

prices = [10, 20, 34]
total = 0
for item in prices:
    total += item

print(f"Total: {total}")


#List of coordinates
for x in range(4):
    for y in range(3):
      print(f"({x}, {y})")


number = [2, 2, 2, 2, 5]
for x in number:
    output = ""
    for y in range(x):
        output += "X"
    print(output)


numbers = [1, 2, 3, 44, 552]
number_highest = numbers[0]
for value in numbers:
    if value > number_highest:
        number_highest = value
print(number_highest)


#2D lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)

numbers = [5, 2, 1, 7, 4]

numbers.append(23)
print(numbers)
numbers.insert(3, 33)
print(numbers)
numbers2 = numbers.copy()
numbers.reverse()
print(numbers)

numbers2.insert(6, 22)
print(numbers2)
values = [2 , 33]
for x in values:
    numbers2.remove(x)
print(numbers2)

numbers = [5, 2, 1, 7, 4, 2, 5]
position = 1
numbers2 = numbers.copy()
for check_number in numbers:
    for x in numbers[position:]:
        if check_number == x:
            print(f"Duplicate number: {x}")
            numbers2.remove(x)
    position += 1
print(numbers2)

numbers = [5, 2, 1, 7, 4, 2, 5]
uniques = []
for check_number in numbers:
    if check_number not in uniques:
        uniques.append(check_number)
print(uniques)


#Tuples
#cannot mutate tuples
numbers = (1, 2, 4)
print(numbers)


#Unpacking
coordinates  = (1, 2, 3)
x, y, z = coordinates               #Unpacking
print(x * y * z)

#Dictonaries
customer = {
    "name": "John Smith",
    "age": 30,
    "is verified": True
}

customer["birthdate"] = "1 1 2000"
print(customer)

number_conversion = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
phone = input("Phone: ")
for number in phone:
    output += number_conversion.get(number, "!") + " "
print(output)


#Emoji Converter
message = input("> ")
words = message.split(" ")
print(words)

emojis = {
    ":)" : ":smile:"
}
output = ""
for word in words:
    output += em.encode(emojis.get(word, word)) + " "
print(output)


#Functions and parameters
def greet_user(first_name, last_name):
    print(f"Hi, {first_name} {last_name}! ")
    print("Welcome aboard! ")

username = input("Hi! What is your name? ")
username = username.split(" ")
print(username)
greet_user(username[0], username[1])                        #positional arguments
greet_user(last_name=username[1], first_name=username[0])   #keyword arguments


def square(number):
    return number ** 2
    return 

print(square(3))


#Exceptions for Error Handling

try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("Age can not be zero! ")
except ValueError:
    print("Invalid Value! ")

'''

#Classes
'''Numbers
Strings
Booleans
-----
Lists
Dictonaries


class Point:                        #Pascal naming convention

    def __init__(self, x, y):             #Constructor
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")

point1 = Point()
point1.draw()
point1.x = 10
print(point1.x)



class Person:
    def __init__ (self, name):
        self.name = name

    def talk(self):
        print(f"Hi, my name is {self.name}. ")

person1 = Person("Michael")
person1.talk()

#Inheritance
class Dog:
    def walk(self):
        print("walk")

class Cat(Dog):
    def run(self):
        print("run")


cat1 = Cat()
cat1.walk()


#Modules
def lbs_to_kg(weight):
    return weight * 0.45


def kg_to_lbs(weight):
    return weight / 0.45

print(con.kg_to_lbs(75))                #imported module converters as con

numbers = [1, 22, 31, 456, 466]
number_highest = con.find_max(numbers)
print(f"The highest number is {number_highest}.  ")


#Packages
shipping.calc_shipping()



#Random values generators
for o in range(3):
    print(random.randint(10,20))

member = ["Marc", "Mao", "Lorn"]
print(random.choice(member))


class Dice:
    def roll(self):
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        return x, y


dice1 = Dice()
print(dice1.roll())
'''

#Files and Directories
#Absolute Paths
#Relative Paths



