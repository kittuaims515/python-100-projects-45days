print("P12_calculator_with_user_choice")
name = str(input("what is your name?\n"))
age = int(input("what is your age?\n"))
first_Value = float(input("Enter the first value:\n"))
second_Value = float(input("Enter the second value:\n"))
#if(second_Value == 0):
#print("You cannot divide by zero")
action = str(input("choose an action: add, sub, mul, div\n"))
print("Hello,", name, "you are doing great with Python!")
print("Your age is: " + str(age + 1))
if(second_Value == 0 and action == "div"):
  print("You cannot divide by zero")
elif(action == "add"):
  print(first_Value + second_Value)
elif(action == "sub"):
  print(first_Value - second_Value)
elif(action == "mul"):
  print(first_Value * second_Value)
elif(action == "div"):
  print(first_Value / second_Value)
  print(round(first_Value / second_Value, 2))
else:
  print("not valid")