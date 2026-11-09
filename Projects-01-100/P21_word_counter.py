import time
print("P21_word_counter.py")
name = input("What is your name?\n")
age = int(input("What is your age?\n"))
sentence = input("Enter your sentence\n").lower().strip()
words = sentence.split()
print(name, "I am splitting your secentence")
time.sleep(3)
print(words)
count = len(words)
print(name, "I am counting the words")
time.sleep(3)
print(count)
print(name + ",your sentence contains", count, "words. Those are", words ) 
if age >=18:
    print("you are eligible for vote")
else:
    print("you are not eligible for vote")