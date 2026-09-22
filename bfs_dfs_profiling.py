from collections import deque
import timeit

# Small graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# BFS
def bfs(graph, start, goal):
    queue = deque([start])
    visited = set()
    nodes_expanded = 0

    while queue:
        node = queue.popleft()

        if node in visited:
            continue

        visited.add(node)
        nodes_expanded += 1

        if node == goal:
            return nodes_expanded

        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)

    return nodes_expanded


# DFS
def dfs(graph, start, goal):
    stack = [start]
    visited = set()
    nodes_expanded = 0

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        nodes_expanded += 1

        if node == goal:
            return nodes_expanded

        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                stack.append(neighbour)

    return nodes_expanded


# Problem
start = 'A'
goal = 'G'

# Run BFS 3 times
bfs_times = timeit.repeat(
    lambda: bfs(graph, start, goal),
    repeat=3,
    number=1000
)

# Run DFS 3 times
dfs_times = timeit.repeat(
    lambda: dfs(graph, start, goal),
    repeat=3,
    number=1000
)

# Convert to milliseconds
bfs_avg = (sum(bfs_times) / len(bfs_times)) * 1000 / 1000
dfs_avg = (sum(dfs_times) / len(dfs_times)) * 1000 / 1000

# Node count
bfs_nodes = bfs(graph, start, goal)
dfs_nodes = dfs(graph, start, goal)

print("----- SLE-2 BFS vs DFS PROFILING -----")

print("\nBFS Results")
print("Average Time:", bfs_avg, "ms")
print("Nodes Expanded:", bfs_nodes)

print("\nDFS Results")
print("Average Time:", dfs_avg, "ms")
print("Nodes Expanded:", dfs_nodes)

print("\nComparison")
if bfs_avg < dfs_avg:
    print("BFS took less time.")
else:
    print("DFS took less time.")

if bfs_nodes < dfs_nodes:
    print("BFS expanded fewer nodes.")
elif dfs_nodes < bfs_nodes:
    print("DFS expanded fewer nodes.")
else:
    print("Both expanded the same number of nodes.")