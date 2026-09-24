# SLE-2: BFS vs DFS Profiling

**Course:** 02AML204 – Introduction to Artificial Intelligence  
**Topic:** Empirical Performance Analysis using BFS and DFS  
**Student:** Anushka  
**PRN:** 25UAM033

## Objective
This project compares Breadth First Search (BFS) and Depth First Search (DFS) on the same small graph using average execution time and nodes expanded. It uses timeit for numerical timing, py-spy for profiler/flame-graph analysis, and a Python graph generator for visual comparison.

The SLE-2 guideline requires both algorithms to be run on the same problem and supported with measured numbers. fileciteturn0file0L49-L68

## Problem Used

```
        A
       / \\
      B   C
     / \\ / \\
    D  E F  G
```

Start node: **A**  
Goal node: **G**

## Algorithms

### BFS
BFS uses a queue and explores nodes level by level.

### DFS
DFS uses a stack and explores one branch before backtracking.

Both implementations use a visited set and count expanded nodes.

## Profiling Tools

### timeit
The Python timeit module is used to run each search repeatedly and calculate average execution time.

### py-spy
Install:

```bash
pip install py-spy
```

Run the program:

```bash
python bfs_dfs_profiling.py
```

Live profiling:

```bash
py-spy top -- python bfs_dfs_profiling.py
```

Create a flame graph:

```bash
py-spy record -o bfs_dfs_flame.svg -- python bfs_dfs_profiling.py
```

Open bfs_dfs_flame.svg in a browser to inspect where execution time is spent.

## Generate the Performance Graph
After running the profiling program, it creates results.csv. Then run:

```bash
python plot_results.py
```

This creates performance_graph.png. The graph is based on actual measured values, not assumed values.

## Results Table

| Metric | BFS | DFS |
|---|---:|---:|
| Average Time (ms) | Run experiment | Run experiment |
| Nodes Expanded | Run experiment | Run experiment |

Do not enter estimated numbers. The SLE-2 guideline specifically requires real profiling numbers. fileciteturn0file0L19-L22

## Best, Average and Worst Case

Theoretical time complexity for graph traversal/search is summarized below:

| Algorithm | Best Case | Average Case | Worst Case |
|---|---|---|---|
| **BFS** | O(1) | O(V + E) | O(V + E) |
| **DFS** | O(1) | O(V + E) | O(V + E) |

Where **V** is the number of vertices (nodes) and **E** is the number of edges.

### BFS
- **Best case:** O(1) when the goal is the starting node.
- **Average case:** O(V + E) when a substantial part of the graph may need to be explored.
- **Worst case:** O(V + E) when the graph is fully explored before the goal is found or determined to be absent.

### DFS
- **Best case:** O(1) when the goal is the starting node or is reached immediately.
- **Average case:** O(V + E), depending on the graph structure and goal location.
- **Worst case:** O(V + E) when the graph may need to be fully explored.

These are theoretical complexity values. The measured execution times in this project are experimental results for the selected graph and should be reported separately.

## Analysis
Identify the algorithm with lower measured execution time from the experiment. Compare the node counts and explain the result using the measured data. For a larger search space, differences between search strategies can become more visible.

## AI Contribution
**AI tool used:** ChatGPT

**AI helped with:**
- Structuring the BFS and DFS profiling code
- Preparing the README and contribution log
- Adding py-spy profiling instructions
- Adding code to generate the performance graph

**My work:**
- Running the code and profiler
- Collecting actual performance values
- Checking the generated graph and flame graph
- Interpreting the experimental results

The SLE-2 guideline asks for an honest AI contribution note and identification of work done by the student. fileciteturn0file0L69-L72

## Files
- bfs_dfs_profiling.py — BFS, DFS, timing and node-count experiment
- plot_results.py — generates the performance graph
- CONTRIBUTION_LOG.md — AI contribution record
- results.csv — generated experimental measurements
- performance_graph.png — generated performance graph
- bfs_dfs_flame.svg — optional py-spy flame graph

## Conclusion
This experiment demonstrates empirical performance analysis of BFS and DFS. It measures actual execution time and nodes expanded on the same graph so the final SLE-2 comparison can be justified with data.