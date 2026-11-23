print("P32_Grocery_Bill_Calculator.py")

groceries = []
item1 = {"item": "Rice", "price": 60, "qt": 2}
item2 = {"item": "Milk", "price": 30, "qt": 3}

groceries.append(item1)
groceries.append(item2)
groceries.append({"item": "Sugar", "price": 45, "qt": 1})

for y in groceries:
    print(y)

answer = input("Do you want to add more items? Enter yes or no: ").lower().strip()
while answer != "yes" and answer != "no":
    print("Invalid input!")
    answer = input("Enter yes or no: ").lower().strip()

if answer == "no":
    for y in groceries:
        print(y)
else:
    while answer == "yes":
        items = input("Enter the item name: ").lower().strip()

        is_valid = False
        while not is_valid:
            try:
                prices = float(input("Enter the price: "))
                if prices <= 0:
                    print("Enter positive numbers only.")
                else:
                    is_valid = True
            except ValueError:
                print("Invalid price! Enter numbers only.")

        is_valid = False
        while not is_valid:
            try:
                qts = int(input("Enter the quantity: "))
                if qts <= 0:
                    print("Enter positive numbers only.")
                else:
                    is_valid = True
            except ValueError:
                print("Invalid quantity! Enter whole numbers only.")

        new_item = {"item": items, "price": round(prices, 2), "qt": qts}
        groceries.append(new_item)
        print("Entered items added to the list:", new_item)

        answer = input("Do you want to add more? (yes/no): ").lower().strip()
        while answer != "yes" and answer != "no":
            print("Invalid input!")
            answer = input("Enter yes or no: ").lower().strip()

print("Total items in list:", len(groceries))

total = 0
for x in groceries:
    cost = x["price"] * x["qt"]
    print("Item:", x["item"], "|", "Quantity:", x["qt"], "|", "Price:", x["price"], "|", "Total:", cost)
    total = total + cost

print("Total cost of all items:", total)