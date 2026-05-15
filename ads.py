def dfs(adj, u, vis, res):
    vis.add(u)
    res.append(u)
    for v in sorted(adj[u]):
        if v not in vis:
            dfs(adj, v, vis, res)
    return res

graph = {
    1: [2, 4], 2: [1, 3, 5], 3: [2, 6],
    4: [1, 5, 7], 5: [2, 4, 6, 8], 6: [3, 5, 9],
    7: [4, 8, 10], 8: [5, 7, 9, 11], 9: [6, 8, 12],
    10: [7, 11], 11: [8, 10, 12], 12: [9, 11]
}

path = dfs(graph, 1, set(), [])
print("DFS Path:", path)