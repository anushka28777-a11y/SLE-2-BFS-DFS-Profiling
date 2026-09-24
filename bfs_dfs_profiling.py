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

def average_time(search_function, runs=3, number=10000):
    measurements = timeit.repeat(
        lambda: search_function(graph, "A", "G"),
        repeat=runs,
        number=number
    )
    return (sum(measurements) / len(measurements)) * 1000 / number

def save_results(bfs_time, dfs_time, bfs_nodes, dfs_nodes):
    with open("results.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Algorithm", "Average Time (ms)", "Nodes Expanded"])
        writer.writerow(["BFS", bfs_time, bfs_nodes])
        writer.writerow(["DFS", dfs_time, dfs_nodes])

def main():
    bfs_time = average_time(bfs)
    dfs_time = average_time(dfs)
    bfs_nodes = bfs(graph, 'A', 'G')
    dfs_nodes = dfs(graph, 'A', 'G')
    save_results(bfs_time, dfs_time, bfs_nodes, dfs_nodes)
    print('----- SLE-2 BFS vs DFS PROFILING -----')
    print(f'BFS Average Time: {bfs_time:.6f} ms')
    print(f'BFS Nodes Expanded: {bfs_nodes}')
    print()
    print(f'DFS Average Time: {dfs_time:.6f} ms')
    print(f'DFS Nodes Expanded: {dfs_nodes}')
    print()
    print('Results saved to results.csv')
    if bfs_time < dfs_time:
        print('BFS took less measured time.')
    elif dfs_time < bfs_time:
        print('DFS took less measured time.')
    else:
        print('Both algorithms took the same measured time.')
    if bfs_nodes < dfs_nodes:
        print('BFS expanded fewer nodes.')
    elif dfs_nodes < bfs_nodes:
        print('DFS expanded fewer nodes.')
    else:
        print('Both algorithms expanded the same number of nodes.')

if __name__ == '__main__':
    main()