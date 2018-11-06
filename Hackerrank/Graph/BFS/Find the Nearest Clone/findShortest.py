from collections import deque

def BFS(mapp, source, val, n, color):
    queue = deque()
    visited = [False]*n
    distance = [float('inf')]*n
    visited[source-1] = True
    distance[source-1] = 0
    queue.append(source)
    while queue:
        fromm = queue.popleft()
        for too in mapp[fromm]:
            if not visited[too-1]:
                visited[too-1] = True
                distance[too-1] = distance[fromm-1] + 1
                queue.append(too)
                if color[too-1] == val:
                    return distance[too-1]

def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    mapp = {}
    for i in range(len(graph_from)):
        if graph_from[i] in mapp:
            mapp[graph_from[i]].append(graph_to[i])
        else:
            mapp[graph_from[i]] = [graph_to[i]]
    for i in range(len(graph_to)):
        if graph_to[i] in mapp:
            mapp[graph_to[i]].append(graph_from[i])
        else:
            mapp[graph_to[i]] = [graph_from[i]]

    distances = []
    rightColorNodes = []
    for i in range(len(ids)):
        # start from all the relevant colors
        if ids[i] == val:
            rightColorNodes.append(i + 1)
    for i in rightColorNodes:
        length = BFS(mapp, i, val, graph_nodes, ids)
        if length:
            distances.append(length)
    if len(distances) == 0:
        return -1
    else:
        return min(distances)