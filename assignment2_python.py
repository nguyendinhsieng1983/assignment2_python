# -*- coding: utf-8 -*-
"""assignment1_python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hak7SkYfxs268npaYgsO0fKdxuHbCwf5

# Data types in Python - Assignment 2
Basics of Data Analysis  <br>
                Total Points 26 <br>
                             ***To pass you need to get atleast 14 points***

Task 1: Create a string (name), an integer (num) and a floating point number (fnum). Assign your name to name, 25 to num and 56.78 to fnum. Print the output for all 3 variables. (6 points)
"""

name = ""
num = 0
fnum = float(num)
print(name)
print(num)
print(fnum)

"""Task 2: Use the capitalize() method to convert the first character of a string to uppercase letter. (1 point)"""

mystring = "this is getting interesting."
mycaptial_string = mystring.capitalize() #use capitalize method
print(mycaptial_string)
#print the capitalized string

"""Task 3: The find() method returns the index of first occurence of the substring if it is found and if it does not find it returns -1. Use find() method to complete the code below. (1 point)"""

text = "Python is an easy to learn language"
result = text.find("learn")#find learn
print(result)

"""Task 4: It is possible to assign the same value to multiple variables at once in Python. Complete the code below. (1 point)"""

# create 3 variables a,b & c &
# assign 1 as value to all variables in the same statement
a=b=c=1
print(a)
print(b)
print(c)

"""Task 5: Complete tasks as in the comment below (5 Points)"""

a = "I like python"
print(len(a)) # use the len method to print the length of the string
print(a[0]) # print the first character of the string
print(a.upper()) # print the string in uppercase letters

"""Task 6: Create a list named mylist and include 5 different data items. (4 points)"""

mylist =  ["item1", "item2", "item3", "item4", "item5"] # it should contain 5 different data items
print(list(mylist)) # print the entire list
print(mylist[1]) # print only the second element
#use append to add one more item to your list
mylist.insert(1, "item1.2")
print(list(mylist)) #print the entire list

"""Task 7: Tuple (3 points)"""

courses = ("Introduction to IoT & Cloud", "Python Basics for IoT", "Python Project")
print(len(courses)) #use len method to print the number of items(courses) in the tuple courses.
print(list(courses)) #print all items in the tuple courses
print(courses[2]) #print the third item in the tuple

"""Task 8: Dictionary (5 points)"""

#create a dictionary with the key as course, time and ects
    #values as Python Basics, Autumn, 5
test = {
  "course" : "Python Basics",
  "time": "Autumn",
  "ects": "5"
}
print(test["course"]) #use get method to print the value of the course
test["course"] = "IoT" #change the course value to Python Basics for IoT

test["pair"] = "year:2019"#add the key/value pair as year:2019 to the test dictionary
print(test) #print the entire dictionary