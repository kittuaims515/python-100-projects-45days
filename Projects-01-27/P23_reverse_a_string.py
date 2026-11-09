import random
import time
print("P23_reverse_a_string.py")
name = input("enter your name:\n").upper().strip()
age = int(input("enter your age:\n"))
print("Hello!", name, "your age is ", age)
text = str(input("enter your sentence\n")).lower().strip()
character_count = (len(text))
time.sleep(2)
print(name, "sentence you have entered is: " + text)
reversed_text = text[::-1]
time.sleep(2)
print(name, "reversed your sentence: " + reversed_text)
print(name, "Character count: " + str(character_count))
print(name, "Word count:",str(len(text.split())))
