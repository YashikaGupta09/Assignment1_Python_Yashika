# Write a python program that checks if two strings are anagrams of each 
# other. 

string1 = input("enter string 1 : ")
string2 = input("enter string 2 : ")

if sorted(string1) == sorted(string2) :
    print("Strings are anagrams.")
else :
    print("Strings are not anagrams.")
