# SLE-2: BFS vs DFS Profiling

**Course:** 02AML204 – Introduction to Artificial Intelligence  
**Topic:** Empirical Performance Analysis using BFS and DFS  
**Student:** Anushka  
**PRN:** 25UAM033

## Objective
This project compares BFS and DFS on the same graph using measured execution time, nodes expanded, and Py-Spy profiling.

## Problem Used
```
        A
       / \
      B   C
     / \ / \
    D  E F  G
```

Start node: **A**  
Goal node: **G**

## Algorithms
- **BFS:** queue-based level-order graph traversal.
- **DFS:** stack-based depth-first graph traversal.
- Both use a visited set and count expanded nodes.

## Profiling with Py-Spy

Install Py-Spy:

```bash
pip install py-spy
```

Run the experiment:

```bash
python bfs_dfs_profiling.py
```

Create the flame graph:

```bash
py-spy record --rate 100 --duration 15 --output bfs_dfs_flame.svg -- python -c "import bfs_dfs_profiling as p; p.profiling_workload()"
```

The profiling workload intentionally repeats BFS and DFS so Py-Spy can collect enough samples. The generated `bfs_dfs_flame.svg` is an actual Py-Spy flame graph and can be opened directly in a browser.

Optional live view:

```bash
py-spy top -- python -c "import bfs_dfs_profiling as p; p.profiling_workload()"
```

## Performance Graph

After running the main program:

```bash
python plot_results.py
```

This reads the measured values from `results.csv`.

## Best, Average and Worst Case

| Algorithm | Best Case | Average Case | Worst Case |
|---|---|---|---|
| **BFS** | O(1) | O(V + E) | O(V + E) |
| **DFS** | O(1) | O(V + E) | O(V + E) |

Here, **V** is the number of vertices and **E** is the number of edges.

## Files
- `bfs_dfs_profiling.py` — BFS, DFS, timing and profiling workload
- `plot_results.py` — performance graph
- `results.csv` — measured timing results
- `performance_graph.svg` — performance graph
- `bfs_dfs_flame.svg` — Py-Spy flame graph
- `CONTRIBUTION_LOG.md` — contribution record

## Important
Run the experiment on your machine before submitting the numerical results. Timing values depend on the computer and Python environment.
