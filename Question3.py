# Write a python program that calculates the factorial of a given number. 

n = int(input("Enter number: "))

factorial = 1

for i in range(1,n+1) :
    factorial = factorial * i

print("Factorial of", n, "is : ", factorial)