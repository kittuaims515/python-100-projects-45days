print("P29_Shopping_List.py")
shopping_list = []
new_item = input("enter the next items:").strip().lower()
while new_item != "done" and new_item != "stop" and new_item != "finished": 
    if new_item != "":
     shopping_list.append(new_item)
    new_item = input("enter the next items:").strip().lower()

print(shopping_list)
count = 1
print("your shopping_list:")
for item in shopping_list:
 print(str(count) + ". " + item)
 count = count + 1


print("Total items are:", len(shopping_list))
 

