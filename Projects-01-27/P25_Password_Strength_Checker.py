print("P25_Password_Strength_Checker.py")
name = input("Enter your name:\n").upper().strip()
passd = input("Enter the password\n")
req_ok = (("A" in passd or "B" in passd or "C" in passd)and("a" in passd or "b" in passd or "c" in passd)and("1" in passd or "2" in passd or "3" in passd)and("!" in passd or "@" in passd or "*" in passd)and(len(passd) >= 8))
final = req_ok
if final:
   print(name, "Password passed all checks.")
else:
   print(name, "Password failed one or more checks.")