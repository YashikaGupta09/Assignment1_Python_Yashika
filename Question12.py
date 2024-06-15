# Write a python program that calculates the sum of the digits of a given number. 

number = int(input("Enter number : "))

sum = 0 

while number != 0 :
    remainder = number % 10
    sum = int(sum + remainder)
    number = number/10

print("Sum of the digits of a given number is", sum)