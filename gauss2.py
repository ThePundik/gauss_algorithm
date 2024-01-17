import numpy as np

def elimination_gauss_basic(matrix):
    n = len(matrix)
    epsilon = 1e-7

    for i in range(n):
        if abs(matrix[i][i]) <= epsilon:
            raise ValueError("Zero division error: |aii| <= epsilon")

        for j in range(i + 1, n):
            factor = matrix[j][i] / matrix[i][i]
            for k in range(i, n + 1):
                matrix[j][k] -= factor * matrix[i][k]

    return back_substitution(matrix)

def elimination_gauss_column_choice(matrix):
    n = len(matrix)
    epsilon = 1e-7

    for i in range(n):
        max_row = i
        for j in range(i + 1, n):
            if abs(matrix[j][i]) > abs(matrix[max_row][i]):
                max_row = j

        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]

        if abs(matrix[i][i]) <= epsilon:
            raise ValueError("Zero division error: |aii| <= epsilon")

        for j in range(i + 1, n):
            factor = matrix[j][i] / matrix[i][i]
            for k in range(i, n + 1):
                matrix[j][k] -= factor * matrix[i][k]

    return back_substitution(matrix)

def elimination_gauss_full_choice(matrix):
    n = len(matrix)
    epsilon = 1e-7

    for i in range(n):
        max_val = 0
        max_row, max_col = -1, -1
        for j in range(i, n):
            for k in range(i, n):
                if abs(matrix[j][k]) > max_val:
                    max_val = abs(matrix[j][k])
                    max_row, max_col = j, k

        if max_val <= epsilon:
            raise ValueError("Zero division error: |aii| <= epsilon")

        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
        for j in range(n + 1):
            matrix[j][i], matrix[j][max_col] = matrix[j][max_col], matrix[j][i]

        for j in range(i + 1, n):
            factor = matrix[j][i] / matrix[i][i]
            for k in range(i, n + 1):
                matrix[j][k] -= factor * matrix[i][k]

    return back_substitution(matrix)

def back_substitution(matrix):
    n = len(matrix)
    x = [0] * n

    for i in range(n - 1, -1, -1):
        x[i] = matrix[i][n] / matrix[i][i]
        for j in range(i - 1, -1, -1):
            matrix[j][n] -= matrix[j][i] * x[i]

    return x

def print_matrix(matrix):
    for row in matrix:
        print(row)

def main():
    method = int(input("Choose method (1: Basic, 2: Column Choice, 3: Full Choice): "))
    user_input = input("Do you want to input your own matrix? (y/n): ")

    if user_input.lower() == 'y':
        n = int(input("Enter the size of the matrix: "))
        matrix = []

        print("Enter the augmented matrix:")
        for _ in range(n):
            row = list(map(float, input().split()))
            matrix.append(row)

    else:
        # Example matrices for testing
        matrix_basic = [
            [2, 3, 4, 5],
            [1, 2, 1, 8],
            [3, 1, 2, 9]
        ]

        matrix_column_choice = [
            [0, 2, 1, 8],
            [1, 2, 3, 11],
            [2, 4, -3, 1]
        ]

        matrix_full_choice = [
            [2, -3, 1, 4],
            [1, 1, 3, 9],
            [4, -2, 2, 1]
        ]

        if method == 1:
            matrix = matrix_basic
        elif method == 2:
            matrix = matrix_column_choice
        elif method == 3:
            matrix = matrix_full_choice
        else:
            print("Invalid method choice.")
            return

    print("Original matrix:")
    print_matrix(matrix)

    if method == 1:
        result = elimination_gauss_basic(matrix)
    elif method == 2:
        result = elimination_gauss_column_choice(matrix)
    elif method == 3:
        result = elimination_gauss_full_choice(matrix)

    print("\nSolution:")
    print(result)

if __name__ == "__main__":
    main()
