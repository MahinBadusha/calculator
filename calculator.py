num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your number: "))


print("/nChoose an operation:")
print("1. ADDITON (+)")
print("2.SUBTRACTION (-)")
print("3.MULTIPLICATION (*)")
print("3.DIVISION (/)")

choice = input(" Enter your choice (1-4):")
if choice == "1":
   print("Answer:", num1+num2)

elif choice == "2":
  print("Answer:", num1-num2)

elif choice == "3":
   print("Answer:", num1*num2) 

elif choice == "4":
   if num2 != 0:
      print("Answer:", num1/num2)
   else:
       print("Error: Cannot divide by zero!")

else:
       print("Invalid Choice")





