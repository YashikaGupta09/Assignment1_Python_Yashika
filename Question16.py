# Write a program in python that counts the frequency of each character in 
# a string. 

string = input("enter string : ")

dict1 = {}

for char in string :
    if char in dict1 :
        dict1[char] += 1
    else :
        dict1[char] = 1


for char,frequency in dict1.items() :
    print("frequency of", char, "is :",frequency)
