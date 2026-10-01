from collections import deque
import csv
import timeit

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": [],
    "F": [],
    "G": []
}

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

def average_time(search_function, runs=5, number=10000):
    measurements = timeit.repeat(
        lambda: search_function(graph, "A", "G"),
        repeat=runs,
        number=number
    )
    return (sum(measurements) / len(measurements)) * 1000 / number

def profiling_workload(iterations=500000):
    # Repeated calls give py-spy enough runtime to sample BFS/DFS.
    for _ in range(iterations):
        bfs(graph, "A", "G")
        dfs(graph, "A", "G")

def save_results(bfs_time, dfs_time, bfs_nodes, dfs_nodes):
    with open("results.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Algorithm", "Average Time (ms)", "Nodes Expanded"])
        writer.writerow(["BFS", f"{bfs_time:.6f}", bfs_nodes])
        writer.writerow(["DFS", f"{dfs_time:.6f}", dfs_nodes])

def main():
    bfs_time = average_time(bfs)
    dfs_time = average_time(dfs)
    bfs_nodes = bfs(graph, "A", "G")
    dfs_nodes = dfs(graph, "A", "G")
    save_results(bfs_time, dfs_time, bfs_nodes, dfs_nodes)

    print("----- SLE-2 BFS vs DFS PROFILING -----")
    print(f"BFS Average Time: {bfs_time:.6f} ms")
    print(f"BFS Nodes Expanded: {bfs_nodes}")
    print()
    print(f"DFS Average Time: {dfs_time:.6f} ms")
    print(f"DFS Nodes Expanded: {dfs_nodes}")
    print()
    print("Results saved to results.csv")
    print()
    print("----- BEST / AVERAGE / WORST CASE COMPLEXITY -----")
    print("BFS: Best O(1), Average O(V + E), Worst O(V + E)")
    print("DFS: Best O(1), Average O(V + E), Worst O(V + E)")

if __name__ == "__main__":
    main()
