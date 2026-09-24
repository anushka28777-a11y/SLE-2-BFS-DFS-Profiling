# Contribution Log — SLE-2

## Project
BFS vs DFS Empirical Performance Analysis

## AI Tool Used
ChatGPT

## Contributions

| Task | AI Contribution | Student Contribution |
|---|---|---|
| BFS/DFS structure | Suggested and organized the search implementations | Reviewed and used the code |
| Profiling | Suggested timeit and py-spy workflow | Run the profiler and inspect the results |
| README | Prepared project documentation structure | Reviewed the documentation |
| Graph | Prepared code to generate a performance graph from measured CSV data | Run the graph script and verify the graph |
| Analysis | Suggested how to connect time and node count to the comparison | Record actual values and write the final interpretation |
| Report | Helped structure the SLE-2 report sections | Prepare and submit the final report |

## Important
The performance values must be obtained by actually running the experiment. No estimated or copied values should be entered in the SLE-2 report.

## Profiling Commands

```bash
python bfs_dfs_profiling.py
py-spy top -- python bfs_dfs_profiling.py
py-spy record -o bfs_dfs_flame.svg -- python bfs_dfs_profiling.py
python plot_results.py
```