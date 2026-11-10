print("P29_Shopping_List.py")
shopping_list = ["Apple","Bags", "Cake"]
shopping_list.append("Butter")
shopping_list.append("Rice")
count = 1
print("your shopping list is:")
for x in shopping_list:
    print(str(count) +"."+ x)
    count = count + 1

print("Total items in shopping list: " + str(len(shopping_list)))
    
