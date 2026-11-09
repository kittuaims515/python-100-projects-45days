print("P19_simple_quiz.py")
print("Welcome to the Python Quiz!\nThis quiz contains 3 questions")
score  = 0
print("What is the Capital of France?")
answer1 = input("Enter your answer:\n").lower().strip()
if answer1 == "paris":
  score = score + 1
  print("Correct", "Your current score is:", score)
else:
  print("Wrong Answer!", "Your current score is:", score)
print("What is 10 + 5:")
answer2 = int(input("Enter your answer:\n"))
if answer2 == 15:
   score = score + 1
   print("Correct", "Your current score is:", score)
else:
  print("Wrong Answer!", "Your current score is:", score)
print("What is output of 3*4:")
answer3 = int(input("Enter your answer here:\n"))
if answer3 == 12:
  score = score + 1
  print("Correct", "Your current score is:", score)
else:
  print("Wrong Answer!", "Your current score is:", score)
print("Your Final Score is:", score)
if(score == 0):
  print("failed")
elif(score == 1):
  print("ok")
elif(score == 2):
  print("good")
else:
  print("Best")
