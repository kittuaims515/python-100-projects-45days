print("P42_Unit_Converter.py")
print("==== UNIT CONVERTER ====")
print("\n 1. Kilometres to Miles\n", "2. Miles to Kilometres\n","3. Celsius to Fahrenheit\n",
      "4. Fahrenheit to Celsius\n","5. Kilograms to Pounds\n","6. Pounds to Kilograms",
"\n=========================")
choice = int(input("Enter your choice (1-6):"))
if choice == 1:
   print("Kilometres to Miles")
   KM = float(input("Enter how many KM you want to convert to miles:"))
   if KM >=0:
    mile = 0.621371
    kilometretoMiles = KM * mile
    print("Kilometres to Miles:", round(kilometretoMiles,2))
   else:
     print("Invalid distance! Negative values are not allowed.")
elif choice == 2:
   print("Miles to Kilometres")
   mile= float(input("Enter how many Miles you want to convert to Kilometres:"))
   if mile >=0:
    kilometer = 1.60934
    MilestoKilometers = kilometer * mile
    print("Miles to Kilometres:", round(MilestoKilometers,2))
   else:
    print("Invalid distance!Negative distance is not allowed.")
elif choice == 3:
   print("Celsius to Fahrenheit")
   cs= float(input("Enter data you want to convert to Fahrenheit:"))
   fh = (cs*9/5)+32
   print("Celsius to Fahrenheit:", round(fh,2))
elif choice == 4:
   print("Fahrenheit to Celsius")
   fh= float(input("Enter data you want to convert to Celsius:"))
   cs = (fh - 32)*5/9
   print("Fahrenheit to Celsius:", round(cs,2))
elif choice == 5:
   print("Kilograms to Pounds")
   kg= float(input("Enter data you want to convert to Pounds:"))
   if kg >=0:
    pd = kg * 2.20462
    print("Kilograms to Pounds:", round(pd,2))
   else:
    print("Invalid input!Negative weight is not allowed.")
elif choice == 6:
   print("Pounds to Kilograms")
   pd= float(input("Enter data you want to convert to Kilograms:"))
   if pd >=0:
    kg = pd * 0.453592
    print("Pounds to Kilograms:", round(kg,2))
   else:
    print("Invalid input!Negative weight is not allowed.")
else:
  print("invalid choice!Please select an option between 1 and 6.")