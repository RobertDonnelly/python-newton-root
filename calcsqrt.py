#! /usr/bin/env python3

# Robert Donnelly
# Calculate square root of a number

def sqrt(x):
    """
    Calculate the square root of argument x.
    """

    #initial gues for square root
    z = x/2.0
    
    #Continuously improve the guess
    #Adadapted from https://tour.golang.org/flowcontrol/8
    while abs(x - (z*z)) > 0.0001: 
     z = z-(z*z - x) / (2*z)
    
    return z
myval=63.00
print("the square root of",myval,"is:",sqrt(myval))


