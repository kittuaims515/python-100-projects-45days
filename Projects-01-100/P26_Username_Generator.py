import time
print("P26_Username_Generator.py")
name = input("Enter your name: \n").lower().strip()
birth_year = input("Enter your birth year: \n").strip()
username = name + birth_year
length = len(username)
print(username)
time.sleep(2)
if length >= 8:
  print("Username length is valid.")
else:
  print("Username is too short.")