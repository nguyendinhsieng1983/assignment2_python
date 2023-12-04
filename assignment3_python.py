Assignment 3 - Control Flow, Loop, Numpy & Function
Basics of Data Analysis
Total Points 26
To pass you need to get atleast 14 points

1. Write a program that prompts students to provide their total points (0 -100) and check with the following conidtions: (5 Points)
if total point is greater than or equal to 85 then the grade is 5
if total point is greater than or equal to 75 then the grade is 4
if total point is greater than or equal to 65 then the grade is 3
if total point is greater than or equal to 55 then the grade is 2
if total point is greater than or equal to 45 then the grade is 1
if total point is less than 45 then the grade is 0
(Use IF statement)

[ ]
#ask user to input point - check example just below this cell if you do not know how to get input from the user.
# Write conditions to check and output the grade based on point
totalPoint = int(input("Enter your total point: "))
if totalPoint >= 85:
    print("Grad is 5")
if totalPoint >= 75:
    print("Grad is 4")
if totalPoint >= 65:
    print("Grad is 3")
if totalPoint >= 55:
    print("Grad is 2")
if totalPoint >= 45:
    print("Grad is 1")
if totalPoint < 45:
    print("Grad is 0")


[ ]
# How to get input from the user in Python?
# To get input from the user , you can use input() function which always returns a string
# Example 1: String input from the user
user_input = input("Enter your name: ")
print("Your name is ", user_input)

# Example 2: Number input from the user
# To get numbers from the user, you will need to conver the user inputs by using functions like int() or float().

# To get an integer input from the user
age_input = int(input("Enter your Age: "))
print("You are ", age_input, "years old.")


# To get a float input from the user
height_input = float(input("Enter your height in cm: "))
print("Your height is ", height_input, "CM")
2. Write a program that asks used to input a number and create the multiplication table (from 1 to 10) of a number.(Use For) The output should be as below for an inputted number: (5 Points)
5 * 1 = 5
5 * 2 = 10
...
...
...
5 * 10 = 50
[ ]
# get input from the user
num = int(input("Enter your number : "))
for x in range(10):
    rangStart = x + 1 
    mul = num * rangStart
    printer = "{} * {} = {}"
    
# print multiplication table for the number
print( printer.format(num, rangStart, mul) )
[ ]

3. Write a program using Numpy to generate and print 5 random number between 1 & 10 (Hints: random.randint) (3 Points)
[ ]

# Generate 5 random numbers between 1 and 10
import numpy as np

numbers = np.random.randint(1, 10, size=5)

# Print the generated numbers
print(numbers)

4. Calculate the mean, media, mode and standard deviation of an array using Numpy. (5 Points)
[ ]
# create a numpy array named numpy_yourfirstName that includes 10 numbers.
import numpy as np
from scipy import stats as st

# create 4 different variables to store mean, median, mode and standard deviation

array = np.arange(20)
print(array)
r1 = np.mean(array)
print("\nMean: ", r1)
r1 = np.median(array)
print("\nMedian: ", r1)
r1 = st.mode(array)
print("\nMode: ", r1)
r1 = np.std(array)
print("\nstd: ", r1)

# print each value in a new line that is:  The Mean is .... The median is .... The mode is .... The standard deviation is ......
5. Generate a numpy array of evenly spaced values from 0 to 10 in increments of 2. Hint: np.arrage (2 Points)
[ ]
# create an array of values from 0 to 10 in increments of 2
import numpy as np
temp = np.arange(start=1, stop=10, step=2)

# print
print(temp)

6. Find the maximum and minimum values in an array. (2 Points)
[ ]
myarray = np.array([12,13,11,5,6,7,8,9,100, 223])
# create two variables to store max and minimum values from the above array
import numpy as np

myarray = np.array([12,13,11,5,6,7,8,9,100, 223])
maxVal = np.max(myarray)
minVal = np.min(myarray)
text = "max {} , min {}"

# Print the maximum and minimum values
print(text.format(maxVal, minVal))

7. Create a simple function to calculate the area of a rectangle. (4 points)
[ ]
length = 5.5
width = 6.5
# Create the function to get the area of the rectangle that is area = length * width
# Check below if you do not know how to create function in python
def rectangleArea(length, width):
    result = length * width
    return result
# Calling the function
area = rectangleArea(5.5, 6.5)
print("rectangle area:", area)


# Call the function and print the aread of the rectangle.
[ ]
# You can create function in Python by using the 'def' keyword.

#Syntax:

# def function_name(parameters):
#  your function

#Example 1 : A simple function to add 2 numbers.

# Creating a function
def add_numbers(a, b):
    result = a + b
    return result

# Calling the function
sum_result = add_numbers(4, 5)
print("Sum:", sum_result)




