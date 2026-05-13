def is_safe(board, row, col, n):
    # Check same column
    for i in range(row):
        if board[i] == col:
            return False

    # Check left diagonal
    for i, j in zip(range(row - 1, -1, -1),
                    range(col - 1, -1, -1)):
        if board[i] == j:
            return False

    # Check right diagonal
    for i, j in zip(range(row - 1, -1, -1),
                    range(col + 1, n)):
        if board[i] == j:
            return False

    return True


def solve_backtracking(n):
    board = [-1] * n

    def solve(row):
        if row == n:
            print("Backtracking Solution:", board)
            return True

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col

                if solve(row + 1):
                    return True

        return False

    solve(0)


def solve_branch_and_bound(n):
    board = [-1] * n

    cols = [False] * n
    diag1 = [False] * (2 * n)  # row + col
    diag2 = [False] * (2 * n)  # row - col + n - 1

    def solve(row):
        if row == n:
            print("Branch & Bound Solution:", board)
            return True

        for col in range(n):
            if (not cols[col] and
                not diag1[row + col] and
                not diag2[row - col + n - 1]):

                # Place queen
                board[row] = col
                cols[col] = True
                diag1[row + col] = True
                diag2[row - col + n - 1] = True

                if solve(row + 1):
                    return True

                # Backtrack
                cols[col] = False
                diag1[row + col] = False
                diag2[row - col + n - 1] = False

        return False

    solve(0)


n = int(input("Enter number of queens: "))

solve_backtracking(n)
solve_branch_and_bound(n)