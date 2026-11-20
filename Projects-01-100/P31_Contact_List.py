print("P31_Contact_List.py")
phonebook=[]
arun = {"name":"arun", "phone":"9876543210"}
ravi = {"name":"ravi", "phone":"9876543211"}
phonebook.append(arun)
phonebook.append(ravi)
phonebook.append({"name":"sita","phone":"9876543212"})
print("length of the phonebook:", len(phonebook))

for contact in phonebook:
 print(contact)
found=False
contact_name= input("enter the name you want to search:").lower().strip()
for contact in phonebook:
  if contact["name"] == contact_name:
    found=True
    print("contact found")
    print(contact)

if found == False:
  print("contact not found")

delete_name= input("enter the name you want to delete :").lower().strip()
delete_index = -1

for contact in phonebook:
    if contact["name"] == delete_name:
        delete_index = phonebook.index(contact)
if delete_index != -1:
  print("contact found!")
  phonebook.pop(delete_index)
else:
  print("Contact not found!")
print(phonebook)