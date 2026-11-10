"""import random
print("Random password generator")
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/~`"
password_length = int(input("Enter the length of the password: "))
count = 1
password1 = ""
password2 = ""
password3 = ""
password4 = ""
password = ""
if password_length<=0:
   print("Enter the numbers from 1 and above")
else: 
  while count <= password_length:
    password1 = password + random.choice(lowercase)
    password2 = password + random.choice(uppercase)
    password3 = password + random.choice(numbers)
    password4 = password + random.choice(symbols)
    count = count + 1
  password = password1 + password2 + password3 + password4
  print(password)"""

import random
print("Random password generator")
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/~`"
password_length = int(input("Enter the length of the password: "))
count = 1
password = ""
if password_length<=0:
   print("Enter the numbers from 1 and above")
else: 
  while count <= password_length:
    password = password + random.choice(lowercase + uppercase + numbers + symbols)
    count = count + 1

print(password)