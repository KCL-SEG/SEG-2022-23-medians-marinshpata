"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""


while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

numbers = sorted(numbers)
if len(numbers) % 2 == 0:
    print(numbers[len(numbers) / 2 - 1] + numbers[len(numbers) // 2] / 2) 
else:
    print(numbers[len(numbers) // 2])





    
