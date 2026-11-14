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
       if len(tasks) == 0:
          print("Your To-Do List is empty! Nothing to remove")
       else:
         remove_choice= int(input("Enter the number of the task you want to remove:"))   
         if remove_choice >= 1 and remove_choice <= len(tasks):  
          list_index = remove_choice-1
          tasks.pop(list_index)
          print("Task removed successfully!")
         else:
          print("Invalid task number!")
    else:
       print('Invalid input, Please enter the menu from choice:')    
             

print("your total tasks:", len(tasks))
"""# Project 30 - To-Do List

print("P30_To_Do_List.py")

# Create an empty list to store tasks
tasks = []

# Initialise variables
new_task = ""
menu_choice = ""

# Repeat the menu until the user selects Exit (3)
while menu_choice != "3":

    # Display the menu options
    print(
        "Enter your choice:\n",
        "1. Add Task\n",
        "2. View Tasks\n",
        "3. Exit\n",
        "4. Remove Task"
    )

    # Get the user's menu choice
    menu_choice = input("Choice: ")

    # OPTION 1: ADD TASK
    if menu_choice == "1":

        # Ask the user to enter a task
        new_task = input("Enter your task to do: ").strip().lower()

        # Check that the task is not empty
        if new_task != "":
            tasks.append(new_task)
            print("Task added successfully!")

    # OPTION 2: VIEW TASKS
    elif menu_choice == "2":

        # Check whether the task list is empty
        if len(tasks) == 0:
            print("Your To-Do List is empty!")

        else:
            print("My To-Do List:")

            # Initialise the numbering counter
            count = 1

            # Display each task with its number
            for items in tasks:
                print(str(count) + ". " + items)

                # Increase the counter
                count = count + 1

    # OPTION 3: EXIT
    elif menu_choice == "3":
        print("Stopped. Bye!")

    # OPTION 4: REMOVE TASK
    elif menu_choice == "4":

        # Check whether there are tasks available
        if len(tasks) == 0:
            print("Your To-Do List is empty! Nothing to remove")

        else:

            # Ask the user which task number to remove
            remove_choice = int(
                input("Enter the number of the task you want to remove: ")
            )

            # Validate the entered task number
            if remove_choice >= 1 and remove_choice <= len(tasks):

                # Convert task number into list index
                list_index = remove_choice - 1

                # Remove the selected task
                tasks.pop(list_index)

                print("Task removed successfully!")

            else:
                print("Invalid task number!")

    # HANDLE INVALID MENU CHOICES
    else:
        print("Invalid input! Please choose from the menu.")

# FINAL SUMMARY
# This section executes after the while loop ends.

print("\n========== FINAL SUMMARY ==========")

# Display the total number of remaining tasks
print("Your total remaining tasks:", len(tasks))

# Display remaining tasks, if any
if len(tasks) == 0:
    print("You have no remaining tasks!")

else:
    print("Your remaining tasks:")

    count = 1

    for items in tasks:
        print(str(count) + ". " + items)
        count = count + 1

print("Thank you for using the To-Do List!")
print("===================================")"""