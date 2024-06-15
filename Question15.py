# Write a program that reads data from a CSV file and prints it to the 
# console.

import csv

with open('csvSampleFile.csv', mode ='r') as file:  
       
    csvFile = csv.reader(file)  
    
    for lines in csvFile :  
        print(lines)
