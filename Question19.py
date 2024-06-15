# Write a python program that removes all punctuation from a given string. 

import string
 
str1 = 'hello, I am your student : "Yashika".'
 
str1 = str1.translate(str.maketrans('', '', string.punctuation))

print(str1)