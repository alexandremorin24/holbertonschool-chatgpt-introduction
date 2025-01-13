#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrement n to avoid infinite loop
    return result

if len(sys.argv) > 1:
    try:
        num = int(sys.argv[1])
        if num < 0:
            print("Error: Factorial is not defined for negative numbers.")
        else:
            f = factorial(num)
            print(f)
    except ValueError:
        print("Error: Please provide a valid integer.")
else:
    print("Usage: ./factorial.py <number>")
