# Using adjacency matrix  to store data in a graph

from collections import deque

class Graph:

    def __init__(self,size):
        self.size = size
        self.matrix = [[0] * self.size for _ in range(self.size)]

    def connect(self, start, end):
        # remember both ways need to be connected
        self.matrix[start - 1][end - 1] = 1
        self.matrix[end - 1][start - 1] = 1

    def find_all_distances(self, startId):
        distance = [-1] * (self.size)
        distance[startId - 1] = 0
        queue = deque()
        queue.append(startId)
        while queue:
            fromm = queue.popleft()
            for i in range(0, self.size):
                if self.matrix[fromm - 1][i] == 1 and distance[i] == -1:
                    distance[i] = distance[fromm - 1] + 6
                    queue.append(i + 1)
        result =  distance[:startId - 1] + distance[startId:]
        print(" ".join(map(str, result)))