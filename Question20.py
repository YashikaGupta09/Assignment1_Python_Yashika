# Write a python program that takes a list of numbers and returns their sum. 

n = int(input("Enter total elements in the list : "))

list1 = []

for i in range(n) :
    element  = int(input("enter element : "))
    list1.append(element)

sum = 0

for i in list1 :
    sum = sum + i

print(sum)
