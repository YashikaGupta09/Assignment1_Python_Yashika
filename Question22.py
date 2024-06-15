# Write a python program that returns the minimum and maximum values 
# in a list of numbers. 

list1 = [1,8,3,0,6,78]
largest = list1[0]
smallest = list1[0]

for i in list1 :
    if i > largest :
        largest = i
    elif i < smallest :
        smallest = i

print("The minimum value is :", smallest, "and the maximum value is :", largest)
