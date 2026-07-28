# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in


def transpose_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    transposed = []

    for j in range(columns):
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
        transposed.append(row)

    return transposed


def add_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    columns = len(matrix_a[0])

    result = []

    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(row)

    return result


def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    columns_a = len(matrix_a[0])
    columns_b = len(matrix_b[0])

    result = []

    for i in range(rows_a):
        row = []

        for j in range(columns_b):
            total = 0

            for k in range(columns_a):
                total += matrix_a[i][k] * matrix_b[k][j]

            row.append(total)

        result.append(row)

    return result


def read_matrix(rows, columns):
    matrix = []

    for i in range(rows):
        while True:
            values = input(f"Enter row {i + 1}: ").split()

            if len(values) == columns:
                row = []
                for value in values:
                    row.append(float(value))
                matrix.append(row)
                break

            print(f"Error: Please enter exactly {columns} values.")

    return matrix


def display_matrix(matrix):
    for row in matrix:
        for value in row:
            if value == int(value):
                print(f"{int(value):6}", end="")
            else:
                print(f"{value:6.2f}", end="")
        print()


if __name__ == "__main__":
    print("PART A — Transpose a Matrix")
    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))

    matrix = read_matrix(rows, columns)

    print("\nOriginal Matrix:")
    display_matrix(matrix)

    transposed = transpose_matrix(matrix)

    print("\nTransposed Matrix:")
    display_matrix(transposed)

    print("\nPART B — Add Two Matrices")
    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))

    print("\nEnter Matrix A:")
    matrix_a = read_matrix(rows, columns)

    print("\nEnter Matrix B:")
    matrix_b = read_matrix(rows, columns)

    added = add_matrices(matrix_a, matrix_b)

    print("\nMatrix A + Matrix B:")
    display_matrix(added)

    print("\nPART C — Multiply Two Matrices")
    rows_a = int(input("Enter number of rows for Matrix A: "))
    columns_a = int(input("Enter number of columns for Matrix A: "))

    print("\nEnter Matrix A:")
    matrix_a = read_matrix(rows_a, columns_a)

    rows_b = int(input("Enter number of rows for Matrix B: "))

    while rows_b != columns_a:
        print(
            f"Error: Matrix B must have {columns_a} rows "
            "because Matrix A has that many columns."
        )
        rows_b = int(input("Enter number of rows for Matrix B: "))

    columns_b = int(input("Enter number of columns for Matrix B: "))

    print("\nEnter Matrix B:")
    matrix_b = read_matrix(rows_b, columns_b)

    multiplied = multiply_matrices(matrix_a, matrix_b)

    print("\nMatrix A x Matrix B:")
    display_matrix(multiplied)
