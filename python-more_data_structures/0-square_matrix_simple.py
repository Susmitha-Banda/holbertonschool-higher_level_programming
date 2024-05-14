#!/usr/bin/python3
def square_matrix_simple(matrix):
    new_matrix = []  # Step 1: Create an empty list for the new matrix

    # Step 2: Iterate over each row in the input matrix
    for row in matrix:
        # Create an empty list for squared values in the current row
        squared_row = []
        # Iterate over each element in the current row
        for num in row:
            # Calculate and append the square of the element
            squared_row.append(num ** 2)
        # Append the list of squared values for the current row
        # to the new matrix
        new_matrix.append(squared_row)

    return new_matrix  # Step 3: Return the new matrix
