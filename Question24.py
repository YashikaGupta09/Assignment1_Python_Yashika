# Write a program that acts as a simple calculator. It should take two 
# numbers and an operator (+, -, *, /) as input and print the result. 

num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))
operator = input("Enter operator (+, -, *, /) : ")

if operator == '+' :
    print("Sum is :", num1 + num2)
elif operator == '-' :
    print("Difference is :", num1 - num2)
elif operator == '*' :
    print("Multiplication is :", num1 * num2)
elif operator == '/' :
    print("Division is :", num1 / num2)
