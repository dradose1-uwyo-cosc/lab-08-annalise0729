# Annalise Gade
# UWYO COSC 1010
# Submission Date: 11/10/24
# Lab 08
# Lab Section: 15
# Sources, people worked with, help given to: N/A
# No further comments


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def number(num):
    try:
        # Try to convert to integer
        final = int(num)
        return final
    except ValueError:
        try:
            # Try to convert to float
            final = round(float(num),1)
            return final
        except ValueError:
            return False

print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

def slope(m, b, x_min, x_max):
    y = []      # initiate list
    m = number(m)
    b = number(b)
    if m != False and b != False:
        try:
            x_min = int(x_min)
            x_max = int(x_max)
        except ValueError:
            print("Please input integers for your bounds")
            return False
    else:
        print("Please enter valid numbers")
        return False
    
    if x_min <= x_max:
        for x in range(x_min, x_max + 1):       # add 1 to max such that x_max is included
            y_new = m*x + b
            y.append(y_new)
        return y
    else:
        print("Please ensure x_min <= x_max")
        return False

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

print("Input values to solve y = mx + b for given range, type 'exit' to quit.\n")
while True:
    m = input("Please input a value for m: ")
    if m.lower() == "exit":
        break
    b = input("Please input a value for b: ")
    if b.lower() == "exit":
        break
    x_min = input("Please input a minimum x value: ")
    if x_min.lower() == "exit":
        break
    x_max = input("Please input a maximum x value: ")
    if x_max.lower() == "exit":
        break
    
    y = slope(m, b, x_min, x_max)
    if y != False:
        print(f"Your y values are: {y}")
    else:
        print("Try again")

print("Exited script")
    
print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

def sqroot(num1):
    num = number(num1)
    if num < 0:
        return False
    else:
        numf = num**0.5
        return numf

def quad(a, b, c):
    a = number(a)
    b = number(b)
    c = number(c)

    if a == False or b == False or c == False:
        print("Please enter valid numbers")
        return False
    else:
        disc = b**2 - 4*a*c
        discrim = sqroot(disc)
        if discrim == False:
            print("The discriminant is negative")
            return False
        else:
            x1 = (-b + discrim)/(2*a)
            x2 = (-b - discrim)/(2*a)
            return x1, x2

print("Input values to solve ax^2 + bx _+ c = 0, type 'exit' to quit. \n")
while True:
    a = input("Please input a value for a: ")
    if a.lower() == "exit":
        break
    b = input("Please input a value for b: ")
    if b.lower() == "exit":
        break
    c = input("Please input a value for c: ")
    if c.lower() == "exit":
        break
    
    if quad(a, b, c) == False:
        print("Try again")
    else:
        x1, x2 = quad(a, b, c)
        print(f"x1 = {round(x1, 2)}, x2 = {round(x2, 2)}")

print("Exited script")