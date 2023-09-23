"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

def findMedian(*args):
    if len(args) % 2 == 0:
        return (args[len(args) - 1] + args[len(args)]) / 2
    else:
        return args[len(args) // 2]

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        findMedian(numbers)



    
