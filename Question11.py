# Write a python program that generates the first n numbers in the 
# Fibonacci sequence. 

number = int(input("Enter number: "))

num1 = 0
num2 = 1
count = 1
nextNum = num2

if number == 1 :
    print("Fibbonacci series of", number, "is :", num1)

else:
    print("Fibbonacci series of", number, "is :")
    while count <= number :
        print(nextNum, end= " ")
        nextNum = num1+num2
        num1 = num2
        num2 = nextNum
        count = count + 1
