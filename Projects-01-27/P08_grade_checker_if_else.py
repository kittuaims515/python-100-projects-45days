"""print("P04_addition_int")
# adding two numbers
# variable is box which stores the data from users
Maths = int(input("enter the maths marks: "))
science = int(input("enter the science marks: "))
score = Maths+science
print("Maths marks are: ", Maths)
print("science marks are: ", science)
print("total Score is:", score)

print("P05_basic_calculator_operations")
#learning calculator
a=int(input("Enter the a value:")) #variable it stores the data #int converts into number #input to take the value from user 
b=int(input("Enter the b value:"))
add = a+b
sub = a-b
mul = a*b
div = a/b
print("addition:", add, "\nsubtraction:", sub, "\nmultiplication:", mul, "\ndivision:", div)

print("P06_even_odd_if_modulo")
name = input("what is your beautiful name:")
print("Hello,",name,"you are learning python")
first_number = int(input("enter your number here:"))
result = first_number%2
if result == 0: print(name, "you have entered the number:", first_number, "which is EVEN number because the result is", result,)
else: print(name, "you have enetred the number:", first_number, "which is ODD number because the result is", result, "not 0")

print("P07_positive_negative_zero")
name = input("What is your Beautiful name?")
print("Hello,", name+",", "you are doing great!")
num = int(input("Enter the number \n"))
if num == 0:
   print("Entered number is", num, "which is a ZERO number")
elif num<0:
   print("Entered number is", num, "which is a NEGITIVE number")
else :
    print("Entered number is", num, "which is a POSITIVE number")
"""
print("P08_grade_checker_if_else")
name = input("what is your name?")
print("Hello!", name+",", "Your are doing wonders with Python!")
marks = int(input("Enter your marks(1 to 100): \n"))
if marks >= 90:
    print("A+ Grade")
elif (marks >=75):
  print("A Grade") 
elif (marks >= 55):
   print("B Grade")
elif (marks >= 35):
   print("C Grade")
else:
   print("Better luck next time")
