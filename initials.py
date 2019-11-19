'''
This program find the initials of the name and display it.
---Program written by Son Nguyen---
'''

#Prompt the user for the name and split it into an array of names
name = input("Enter your name: ")
initial = ""
name = name.split()

#Find the first letter in each names and add it to a string
for letter in name:
    initial = initial + letter[0]

#Display the string of initials
print(initial)
