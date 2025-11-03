def count_paths(n, m):

    # Base case: only one way if in the last row or column

    if n == 1 or m == 1:

        return 1

    # Recursive case: move right or down

    return count_paths(n - 1, m) + count_paths(n, m - 1)



# Example: 3x3 maze

rows = 3

cols = 3

print("Total ways to escape the maze:")