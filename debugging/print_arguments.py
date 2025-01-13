#!/usr/bin/python3
import sys

# Start iterating from the second element to exclude the script name
for arg in sys.argv[1:]:
    print(arg)
