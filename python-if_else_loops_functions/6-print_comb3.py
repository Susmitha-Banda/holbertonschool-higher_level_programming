#!/usr/bin/python3
# Initialize count for print statements
print_count = 0

# Iterate over the first digit (i)
for i in range(10):
    # Iterate over the second digit (j)
    for j in range(i + 1, 10):  # Start from i+1 to ensure j > i
        # Print the combination
        print("{:d}{:d}".format(i, j), end="")
        print_count += 1
        
        # Print a comma and space if this is not the last combination
        if print_count < 45:  # 45 combinations: (10*9) / 2
            print(", ", end="")
        else:
            print()  # Print a new line at the end
