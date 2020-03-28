def unique_path(grid):
    rows = len(grid)
    columns = len(grid[0])
    if rows <= 0 or columns <= 0:
        return 0
    dp = [[0] * columns for x in range(rows)]
    # initialize first column for dp
    i = 0
    while i < rows and grid[i][0] == 0:
        dp[i][0] = 1
        i += 1
    # initialize first row for dp
    j = 0
    while j < columns and grid[0][j] == 0:
        dp[0][j] = 1
        j += 1

    for i in range(1, rows):
        for j in range(1, columns):
            if grid[i][j] == 0:
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

    return dp[-1][-1]