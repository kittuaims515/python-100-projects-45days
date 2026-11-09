import random
import time
print("P24_Palindrome_Checker.py")
text = input("Enter the word:\n").lower().strip().replace(" ","").replace("!","")
check = text[::-1]
print(text, check)
if text == check:
    print("your word is palindrome:", text, check)
else:
    print("your word is not palindrome")