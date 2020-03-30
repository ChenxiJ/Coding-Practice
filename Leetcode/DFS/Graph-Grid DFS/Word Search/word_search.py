def search(i, j, board, word_index, word):
    rows = len(board)
    columns = len(board[0])
    if i < 0 or j < 0 or i >= rows or j >= columns:
        return False
    if board[i][j] != word[word_index]:
        return False
    # here means board[i][j] == word[word_index], check whether the end of the word
    if word_index == len(word) - 1:
        return True
    # very important tip that no need to keep an extra variable to store whether the char has been visited, mark as 0
    # so it wont be matched, and when next char not found means this path doesn't work, then mark this current one back

    # here means board[i][j] == word[word_index] so found the current word[word_index] but not the end, look for next
    cur = board[i][j]
    board[i][j] = 0
    found = search(i - 1, j, board, word_index + 1, word) or search(i, j + 1, board, word_index + 1, word) or \
            search(i + 1, j, board, word_index + 1, word) or search(i, j - 1, board, word_index + 1, word)
    board[i][j] = cur
    return found


def exist(board, word):
    rows = len(board)
    columns = len(board[0])
    for i in range(rows):
        for j in range(columns):
            # stack is handled by recursion, no need to explicitly put word to explore in stack
            # start from the first word_index to explore
            if search(i, j, board, 0, word):
                # this is to try all the board cell to be the starting point of the word. if found word starting from (0, 0)
                # return True, otherwise increment i and j
                return True
    return False
