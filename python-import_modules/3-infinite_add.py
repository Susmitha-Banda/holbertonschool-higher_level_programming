#!/usr/bin/python3
# output = addition of all args
# we can cast args using int()
# no execution when imported
import sys
def main():
    # Initialize the sum
    total = 0  
    # Loop through command-line arguments (excluding the script name)
    for arg in sys.argv[1:]:
        # Convert each argument to an integer and add it to the total
        total += int(arg)
    # Print the total sum
    print(total)
if __name__ == "__main__":
    main()
