import random
import time
print("P22_character_counter.py")
name = input("Enter your name:\n").upper().strip()
age = int(input("Enter your age:\n"))
text = input("Enter your statement here\n").lower()
print(text)
time.sleep(2)
print(name, "Total characters of the text is: ",float(len(text)))
time.sleep(3)
print(name, "Words in the statement is: " + str(len(text.split())))
time.sleep(4)
print(name, "The words of the statement are:" + str(text.split()))
time.sleep(2)
if age <= 5:
    print("Kid")
elif age <=11:
    print("kids")
else:
    print("kidss")