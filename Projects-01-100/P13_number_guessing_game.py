"""import random
print("P13_number_guessing_game.py")
name = input("What is your name?\n")
age = int(input("What is your age?\n"))
number = random.randint(1, 10)
print("The number is:", number)
first_value = float(input("Enter first value:\n"))
second_value = float(input("Enter second value:\n"))
operation = str(input("Enter add, sub, mal, div:\n"))
secret = int(input("enter your number:"))
add = first_value + second_value
sub = second_value - first_value
mul = first_value * second_value
div = second_value / first_value
print("Hello,", name+",","You are doing great with Python!" )
print("your age:" +str(age+1))
print("first_value: " +str(first_value), "\nsecond_value: " +str(second_value))
print(number == secret)
if(second_value == 0 and operation == "div"):
    print("second value cannot be 0")
if(first_value>second_value):
    print("second_value should be greater than") 
elif(operation == "add"):
    print(round(add, 0))
elif(operation == "sub"):
    print(round(sub,0))
elif(operation == "mul"):
    print(round(mul,0))
elif(operation == "div"):
    print(round(div,2))
else:
    print("invalid input")"""
import random
number = random.randint(1, 5)
secret = int(input("enter your number:"))
if(number != secret):
    print("Wrong, try again!, the correct number is:", number)
else:
    print("correct:", number)
print(round(25.9))
print(round(25.4))
print(round(22.2))
number = 18.7
print(round(number, 0))
print(int(number))