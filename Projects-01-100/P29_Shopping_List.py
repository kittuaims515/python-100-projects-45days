print("P29_Shopping_List.py")
shopping_list = []
new_item = input("enter the items:").strip().lower()
while new_item != "done" and new_item != "stop" and new_item != "finished": 
    shopping_list.append(new_item)
    new_item = input("enter the next items:").strip().lower()
print("your shopping_list:")
print(shopping_list)
print("Total items are:", len(shopping_list))

