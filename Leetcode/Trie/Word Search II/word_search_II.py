# the first solution is to do dfs search on every word in the list like in the previous one, but will time out. the code
# can be optimized using a Trie for when words sharing prefix


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


# build a trie using the words in the list
def build_trie(words):
    root = TrieNode()
    for word in words:
        cur = root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = word  # this is a alternative to represent whether the node is the end of a word
    return root


def find_words(board, words):
    ans = []
    rows = len(board)
    columns = len(board[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    root = build_trie(words)

    # search in the board for the words in Trie, just need to search one time for all the words
    def search_word(i, j, node):
        char = board[i][j]
        cur_node = node.children[char]
        if cur_node.word:
            ans.append(cur_node.word)
            cur_node.word = None

        board[i][j] = 0
        for di, dj in directions:
            new_row = i + di
            new_column = j + dj
            if 0 <= new_row < rows and 0 <= new_column < columns and board[new_row][new_column] in cur_node.children:
                search_word(new_row, new_column, cur_node)
        board[i][j] = char

    for r in range(rows):
        for col in range(columns):
            if board[r][col] in root.children:
                search_word(r, col, root)
    return ans

### end of solution


# simple dfs will time out, just keep here for reference
def search2(i, j, board, word_index, word):
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
    found = search2(i - 1, j, board, word_index + 1, word) or search2(i, j + 1, board, word_index + 1, word) or \
            search2(i + 1, j, board, word_index + 1, word) or search2(i, j - 1, board, word_index + 1, word)
    board[i][j] = cur
    return found


def findWords(board, words):
    ans = []
    rows = len(board)
    columns = len(board[0])
    for word in words:
        for i in range(rows):
            for j in range(columns):
                # stack is handled by recursion, no need to explicitly put word to explore in stack
                # start from the first word_index to explore
                if search2(i, j, board, 0, word):
                    # this is to try all the board cell to be the starting point of the word. if found word starting from (0, 0)
                    # return True, otherwise increment i and j
                    ans.append(word)
                    # the important part here is once found a match need to stkip the traverse of the board
                    break
                else:
                    continue
            else:
                continue
            break
    return ans
