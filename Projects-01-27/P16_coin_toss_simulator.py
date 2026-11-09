import random
print("P16_coin_toss_simulator.py")
name = str(input("What is your name?\n"))
age = int(input("Wha is your age?\n"))
Toss = random.choice(["heads", "tails", "Coin tossed is went into sky"])
print("Hello,", name, "You will create wonders in future with python")
print("your age is: " + str(age+5))
choice = str(input("Select Toss: heads or tails\n"))
print("Toss is:", Toss)
if (Toss == "Coin tossed is went into sky"):
    print("match abandonded")
elif(choice == Toss):
    print("you have won the toss")
else:
    print("you have lost the toss")
