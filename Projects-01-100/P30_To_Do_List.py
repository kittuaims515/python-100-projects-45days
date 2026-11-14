print("P30_To_Do_List.py")
tasks = []
new_task = ""
menu_choice = ""
while menu_choice != "3":
    print("Enter your choice: \n", "1.Add Task\n", "2.View Tasks\n", "3.Exit \n", "4.Remove Task")
    menu_choice = input("Choice: ")
    if  menu_choice == "1":
      new_task = input("Enter your task to do:").strip().lower()
      if new_task != "":
        tasks.append(new_task)
    elif menu_choice == "2":
      if len(tasks) == 0:
         print("Your To-Do List is empty!")
      else:   
         print("My To-Do List:") 
         count = 1
         for items in tasks:
          print(str(count) + ". " + items)
          count = count + 1  
    elif menu_choice == "3":
        print("Stopped. Bye!")
    elif menu_choice == "4":
       remove_choice= int(input("Enter the number of the task you want to remove:"))
       list_index = remove_choice-1
       tasks.pop(list_index)
       print("Task removed successfully!")
    else:
       print('Invalid input, Please enter the menu from choice:')    
             

print("your total tasks:", len(tasks))
