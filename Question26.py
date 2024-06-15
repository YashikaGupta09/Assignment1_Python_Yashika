# Write a program in python that checks if a string starts with a given prefix 
# or ends with a given suffix. 

string = input("Enter the string: ")

prefix = input("Enter the prefix to check: ")
suffix = input("Enter the suffix to check: ")

for i in range(len(prefix)) :
    if string[i] != prefix[i] :
        print("Prefix doesn't match")
        break
    else :
        print("Prefix matched")
        break

for i in range(len(suffix)) :
    if string[-len(suffix) + i] != suffix[i] :
        print("Suffix doesn't match")
        break
    else :
        print("Suffix matched")
        break
