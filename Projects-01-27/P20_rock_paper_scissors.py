import random
import time
print("P20_rock_paper_scissors.py")
name = str(input("What is your name?\n"))
age = int(input("What is your age?\n"))
print("Hello," + name, "Welcome to Rock Paper Scissors!" )
print("Your age is:", age+1)
score = 0
comp = random.choice(["rock","paper", "scissors"])
player = input("Enter your choice here:\n").lower().strip()
print("Your choice is:", player)
time.sleep(3)
if (player != "rock") and (player != "scissors") and (player != "paper"):
   print("Invalid Input")
elif (player==comp):
   print("Comp choice is:", comp, "Draw!") 
elif (player == "rock" and comp == "scissors") or (player == "paper" and comp == "rock") or (player== "scissors" and comp == "paper"):
   score = score + 1
   print("Comp choice is:", comp, "You win!", score)
else:
   print("Comp choice is:", comp, "You Lose !")

print()



"""elif (player != "rock") and (player != "scissors") and (player != "paper"):
 print("Invalid Input")"""