#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

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
    print("Usage: ./factorial.py <non-negative integer>")
