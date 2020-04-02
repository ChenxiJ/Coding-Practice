def shortest_path(n, i_start, j_start, i_end, j_end):
    path = False
    queue = [(i_start, j_start)]
    # visited = {cur: prev}
    visited = {(i_start, j_start): (-1, -1)}
    directions = [(-2, -1), (-2, 1), (0, 2), (2, 1), (2, -1), (0, -2)]
    count = 0

    def next_step(curr):
        next_steps = []
        for direction in directions:
            new_cell = (curr[0] + direction[0], curr[1] + direction[1])
            if 0 <= new_cell[0] < n and 0 <= new_cell[1] < n and new_cell not in visited:
                next_steps.append(new_cell)
        return next_steps

    while len(queue) > 0:
        pos = queue.pop(0)
        if pos == (i_end, j_end):
            path = True
            break

        for step in next_step(pos):
            queue.append(step)
            visited[step] = pos

    if path:
        dic = {(-2, -1): 'UL', (-2, 1): 'UR', (0, 2): 'R', (2, 1): 'LR', (2, -1): 'LL', (0, -2): 'L'}
        prev = visited[(i_end, j_end)]
        route = [(i_end, j_end)]
        while not prev == (-1, -1):
            count += 1
            route.append(prev)
            prev = visited[prev]
        print(count)
        for i in range(len(route)-1, 0, -1):
            print(dic[(route[i-1][0] - route[i][0], route[i-1][1] - route[i][1])], end=' ')

    else:
        print('Impossible')
