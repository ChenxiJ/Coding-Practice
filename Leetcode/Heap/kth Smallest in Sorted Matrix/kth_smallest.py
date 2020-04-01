from heapq import heappop, heappush


def kth_smallest(matrix, k):
    length = len(matrix)
    visited = {}
    min_heap = []
    smallest = matrix[0][0]
    heappush(min_heap, (smallest, 0, 0))
    visited[(0, 0)] = True

    while k > 0:
        val, row, col = heappop(min_heap)
        if row + 1 < length and (row + 1, col) not in visited:
            heappush(min_heap, (matrix[row + 1][col], row + 1, col))
            visited[(row + 1, col)] = True

        if col + 1 < length and (row, col + 1) not in visited:
            heappush(min_heap, (matrix[row][col + 1], row, col + 1))
            visited[(row, col + 1)] = True
        k -= 1
    return val
