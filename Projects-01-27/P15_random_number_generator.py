import random
print("P15_random_number_generator.py")
name = str(input("What is your name?\n"))
age = int(input("What is your age\n"))
print("Hello,", name, "Your are doing fab with PYTHON")
print("Your age is:" + str(age + 10 -5))
print(round(100.23, 0)) 
print(int(3215.3698))
print(round(10.2))
print(round(20.369))
print(round(36.269,1))
min_Value = int(input("Enter the minimum value:\n"))
max_Value = int(input("Enter the maximum value:\n"))
print("minumum value is:\n", min_Value)
print("maximum value is:\n", max_Value)
if(max_Value == min_Value):
    print(max_Value, "is equals to", min_Value )
elif(max_Value<min_Value):
    print(max_Value, "cannot be less than", min_Value)
else:
    number = random.randint(min_Value, max_Value)
    print(number)