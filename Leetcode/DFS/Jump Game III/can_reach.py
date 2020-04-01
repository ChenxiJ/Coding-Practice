def can_reach(arr, start):
    visited = [False] * len(arr)

    def dfs(s):
        if s < 0 or s >= len(arr):
            return False
        if arr[s] == 0:
            return True
        if visited[s]:
            return False
        visited[s] = True
        return dfs(s + arr[s]) or dfs(s - arr[s])

    return dfs(start)