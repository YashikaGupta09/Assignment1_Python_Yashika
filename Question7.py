# Write a python program that takes a string as input and returns its length.

word = str(input("Enter any word : "))

count = 0

for i in word :
    count = count + 1

print("The length of", word, "is :", count)
