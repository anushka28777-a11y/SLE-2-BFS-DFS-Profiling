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

def measure_time(search_function, start, goal, runs=5, number=10000):
    measurements = timeit.repeat(
        lambda: search_function(graph, start, goal),
        repeat=runs,
        number=number
    )
    return (sum(measurements) / len(measurements)) * 1000 / number

def best_average_worst(search_function):
    best = measure_time(search_function, "A", "A")
    average = measure_time(search_function, "A", "E")
    worst = measure_time(search_function, "A", "Z")
    return best, average, worst

def profiling_workload(iterations=500000):
    for _ in range(iterations):
        bfs(graph, "A", "G")
        dfs(graph, "A", "G")

def save_results(bfs_cases, dfs_cases):
    with open("results.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Algorithm", "Case", "Average Time (ms)", "Nodes Expanded"])
        for algorithm, search_function, cases in [
            ("BFS", bfs, bfs_cases),
            ("DFS", dfs, dfs_cases)
        ]:
            for case_name, start, goal, measured_time in cases:
                nodes = search_function(graph, start, goal)
                writer.writerow([algorithm, case_name, f"{measured_time:.6f}", nodes])

def main():
    bfs_best, bfs_average, bfs_worst = best_average_worst(bfs)
    dfs_best, dfs_average, dfs_worst = best_average_worst(dfs)

    bfs_cases = [
        ("Best", "A", "A", bfs_best),
        ("Average", "A", "E", bfs_average),
        ("Worst", "A", "Z", bfs_worst)
    ]
    dfs_cases = [
        ("Best", "A", "A", dfs_best),
        ("Average", "A", "E", dfs_average),
        ("Worst", "A", "Z", dfs_worst)
    ]

    save_results(bfs_cases, dfs_cases)

    print("----- SLE-2 BFS vs DFS PROFILING -----")
    print()
    print("BFS")
    print(f"Best Case    : {bfs_best:.6f} ms")
    print(f"Average Case : {bfs_average:.6f} ms")
    print(f"Worst Case   : {bfs_worst:.6f} ms")
    print()
    print("DFS")
    print(f"Best Case    : {dfs_best:.6f} ms")
    print(f"Average Case : {dfs_average:.6f} ms")
    print(f"Worst Case   : {dfs_worst:.6f} ms")
    print()
    print("----- TIME COMPLEXITY -----")
    print("BFS: Best O(1), Average O(V + E), Worst O(V + E)")
    print("DFS: Best O(1), Average O(V + E), Worst O(V + E)")
    print()
    print("Results saved to results.csv")

if __name__ == "__main__":
    main()
