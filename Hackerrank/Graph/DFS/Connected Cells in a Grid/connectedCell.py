# connectedCell and DFS are to find the maximum num of cells in a region

def connectedCell(matrix):
    row = len(matrix)
    column = len(matrix[0])
    maxx = 0
    for ro in range(row):
        for col in range(column):
            if matrix[ro][col] == 1:
                maxx = max(maxx, DFS(ro, col, matrix, row, column))
    return maxx

def DFS(ro, col, matrix, row, column):
    if ro < 0 or col < 0 or ro > row - 1 or col > column - 1:
        return 0
    if matrix[ro][col] != 1:
        return 0

    count = 1
    matrix[ro][col] = 2
    count += DFS(ro - 1, col - 1, matrix, row, column)
    count += DFS(ro, col - 1, matrix, row, column)
    count += DFS(ro + 1, col - 1, matrix, row, column)
    count += DFS(ro - 1, col, matrix, row, column)
    count += DFS(ro + 1, col, matrix, row, column)
    count += DFS(ro - 1, col + 1, matrix, row, column)
    count += DFS(ro, col + 1, matrix, row, column)
    count += DFS(ro + 1, col + 1, matrix, row, column)
    return count

# If want to calculate how many regions, use countRegion and DFS2

def countRegion(matrix):
    row = len(matrix)
    column = len(matrix[0])
    count = 0
    for ro in range(row):
        for col in range(column):
            if matrix[ro][col] == 1:
                DFS2(ro, col, matrix, row, column)
                count += 1
    return count


def DFS2(ro, col, matrix, row, column):
    if ro < 0 or col < 0 or ro > row - 1 or col > column - 1:
        return
    if matrix[ro][col] == 1:
        matrix[ro][col] = 2
        DFS2(ro - 1, col - 1, matrix, row, column)
        DFS2(ro, col - 1, matrix, row, column)
        DFS2(ro + 1, col - 1, matrix, row, column)
        DFS2(ro - 1, col, matrix, row, column)
        DFS2(ro + 1, col, matrix, row, column)
        DFS2(ro - 1, col + 1, matrix, row, column)
        DFS2(ro, col + 1, matrix, row, column)
        DFS2(ro + 1, col + 1, matrix, row, column)