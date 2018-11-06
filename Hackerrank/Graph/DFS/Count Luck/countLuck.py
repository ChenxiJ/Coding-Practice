def directionsPossible(matrix, visited, cell):
    rows = len(matrix)
    columns = len(matrix[0])
    # up, down, left, right order
    direction = [0] * 4
    possibles = []
    if cell[0] - 1 >= 0 and matrix[cell[0] - 1][cell[1]] != 'X' and visited[cell[0] - 1][cell[1]] != 1:
        direction[0] = 1
        possibles.append(0)
    if cell[0] + 1 < rows and matrix[cell[0] + 1][cell[1]] != 'X' and visited[cell[0] + 1][cell[1]] != 1:
        direction[1] = 1
        possibles.append(1)
    if cell[1] - 1 >= 0 and matrix[cell[0]][cell[1] - 1] != 'X' and visited[cell[0]][cell[1] - 1] != 1:
        direction[2] = 1
        possibles.append(2)
    if cell[1] + 1 < columns and matrix[cell[0]][cell[1] + 1] != 'X' and visited[cell[0]][cell[1] + 1] != 1:
        direction[3] = 1
        possibles.append(3)
    return direction, possibles


def nextCell(cell, direction):
    if direction[0] == 1:
        return [cell[0] - 1, cell[1]]
    if direction[1] == 1:
        return [cell[0] + 1, cell[1]]
    if direction[2] == 1:
        return [cell[0], cell[1] - 1]
    if direction[3] == 1:
        return [cell[0], cell[1] + 1]
    else:
        return [-1, -1]


def countLuck(matrix, k):
    wandUsed = 0
    rows = len(matrix)
    columns = len(matrix[0])
    start = []
    end = []
    futureChoices = []
    path = []
    # 0 means not visited, 1 means visited
    visited = [[0] * columns for i in range(rows)]
    wand = [[0] * columns for i in range(rows)]
    wandCells = []
    for row in range(rows):
        if len(start) == 0 or len(end) == 0:
            for column in range(columns):
                if len(start) == 0 or len(end) == 0:
                    if matrix[row][column] == 'M':
                        start = [row, column]
                    if matrix[row][column] == '*':
                        end = [row, column]
                else:
                    break
        else:
            break

    next = start
    while next != end:
        path.append(next)
        visited[next[0]][next[1]] = 1
        direction, possibles = directionsPossible(matrix, visited, next)
        if len(possibles) > 1:
            if wand[next[0]][next[1]] == 0:
                # when there is more choices at a cell, then use wand
                # but if returned to a cell that used wand before, cannot count twice
                # also have to delete the wand uses at the cell actually not in the final path!!!
                wandUsed += 1
                wand[next[0]][next[1]] = 1
                wandCells.append(next)
                for i in range(len(possibles) - 1, 0, -1):
                    directionPossible = [0] * 4
                directionPossible[possibles[i]] = 1
                nextPossible = nextCell(next, directionPossible)
                # when add nextPossibles to the stack, need to mark at which cell they are added
                # so when popped back to here, delete everything after that cell from the path
                # since in reality they are not part of the right path
                futureChoices.append([next, nextPossible])

        next = nextCell(next, direction)
        while next == [-1, -1]:
            nextCellWithRecord = futureChoices.pop()
            next = nextCellWithRecord[1]
            for i in range(len(path)):
                if path[i] == nextCellWithRecord[0]:
                    index = i
                    break
            del path[index + 1:]

    for i in wandCells:
        if i not in path:
            wandUsed -= 1

    if k == wandUsed:
        return 'Impressed'
    else:
        return 'Oops!'