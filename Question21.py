# Write a python program that counts the occurrences of a specific element 
# in a list. 

list1 = [2,2,4,5,6,6,9,9]

number = int(input("Enter element to find frequency : "))

frequency = 0

for i in list1 :
    if i == number :
        frequency += 1

print("frequency of", number, "is :",frequency)
