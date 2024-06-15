# Write a program in python that converts a given string to title case (first 
# letter of each word capitalized). 

string = input("Enter your string : ")

string = string[0].upper() + string[1:]

i = 1
while i < len(string) :
    if string[i] == " " and i + 1 < len(string):
        string = string[:i+1] + string[i+1].upper() + string[i+2:]
    
    i = i + 1

print(string)