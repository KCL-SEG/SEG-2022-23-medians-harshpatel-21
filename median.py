"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = sorted([*map(float,input().split(','))])
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        n = len(numbers)
        print(numbers[n//2] if n%2 else (numbers[n//2-1]+numbers[n//2])/2)


