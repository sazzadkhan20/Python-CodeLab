def is_safe(board, row, col):
    """
    Check if placing a queen at board[row][col] is safe.
    """
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_queens(board, col, solutions):
    """
    Use backtracking to solve the 8 Queens Problem.
    """
    n = len(board)

    # Base case: All queens are placed
    if col >= n:
        # Add the current board configuration to the solutions
        solutions.append([row[:] for row in board])
        return

    # Try placing a queen in each row of this column
    for i in range(n):
        if is_safe(board, i, col):
            # Place the queen
            board[i][col] = 1

            # Recur to place the rest of the queens
            solve_queens(board, col + 1, solutions)

            # Backtrack: Remove the queen
            board[i][col] = 0

def print_solutions(solutions):
    """
    Print all solutions in a readable format.
    """
    for index, solution in enumerate(solutions, start=1):
        print(f"Solution {index}:")
        for row in solution:
            print(" ".join("Q" if cell == 1 else "." for cell in row))
        print()

def main():
    n = 8  # Size of the board (8x8)
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    solve_queens(board, 0, solutions)

    print(f"Total solutions found: {len(solutions)}\n")
    print_solutions(solutions)

if __name__ == "__main__":
    main()
