"""
N-Queens Problem (Constraint Satisfaction Problem)
-----------------------------------------------------
AI Practical - Search Algorithm
Author : Niharika Acharya
Algorithm : Backtracking
Language : Python 3
"""


def print_board(board, n):
    """Print the chessboard with Queens."""
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print()


def is_safe(board, row, col, n):
    """Check whether a queen can be placed at board[row][col]."""

    # Check left side of the current row
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    # Check lower-left diagonal
    i, j = row, col
    while i < n and j >= 0:
        if board[i][j]:
            return False
        i += 1
        j -= 1

    return True


def solve_n_queens(board, col, n):
    """Solve the N-Queens problem using Backtracking."""

    # Base case: All queens are placed
    if col == n:
        return True

    # Try placing queen in each row
    for row in range(n):
        if is_safe(board, row, col, n):

            # Place queen
            board[row][col] = 1

            # Recur for next column
            if solve_n_queens(board, col + 1, n):
                return True

            # Backtrack
            board[row][col] = 0

    return False


def get_valid_n():
    """
    Keep asking the user for input until a valid value of N is given.
    N must be a positive whole number (N = 0 is not meaningful here,
    since there is no board to place queens on).
    """
    while True:
        try:
            value = int(input("Enter the value of N: "))
            if value <= 0:
                print("Please enter a number greater than 0.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main():
    n = get_valid_n()

    if n in (2, 3):
        print(f"\nNote: No solution exists for N = {n}.")

    board = [[0 for _ in range(n)] for _ in range(n)]

    if solve_n_queens(board, 0, n):
        print("\nSolution Found:\n")
        print_board(board, n)
    else:
        print("\nNo solution exists.")


if __name__ == "__main__":
    main()
