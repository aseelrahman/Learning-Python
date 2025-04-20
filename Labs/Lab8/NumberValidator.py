print("** ENTER ONLY WHOLE NUMBERS **", end="\n\n")

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Check if both inputs are whole numbers
if num1.isdigit() and num2.isdigit():
    print(f"The product of both numbers is: {int(num1) * int(num2)}")
elif not num1.isdigit() and not num2.isdigit():
    print("Both numbers need to be whole numbers.")
elif not num1.isdigit():
    print("The first number needs to be whole number.")
elif not num2.isdigit():
    print("The second number needs to be whole number.")