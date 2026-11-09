"""import random
import time
print("P18_countdown_timer.py")
name = str(input("What is your name?\n"))
print(name)
number = int(input("age:\n"))
print(number)
r_num = random.randint(1, 10)
r_cho = random.choice(["Heads", "Tails"])
print(r_cho.lower())
print(r_cho.upper())
print(round(18.3))
print(r_num)
print("Timer starts in:", r_num+1, " seconds")
time.sleep(r_num+1)
print("stop")"""
import random
import time

print("P18_countdown_timer.py")

name = input("What is your name?\n").strip()

print("Hello,", name.upper())

seconds = float(input("Enter the timer duration in seconds:\n"))

seconds = round(seconds, 2)

print("Your timer duration is:", seconds, "seconds")

random_number = random.randint(1, 5)

random_choice = random.choice(["Ready", "Set", "Go"])

print("Random number:", random_number)
print("Random message:", random_choice.lower())

print("\nTimer starts now!")

time.sleep(seconds)

print("\nTime's up,", name + "!")

print("Thank you for practising Python!")