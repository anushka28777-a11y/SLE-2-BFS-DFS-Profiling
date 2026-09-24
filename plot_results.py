import csv
import matplotlib.pyplot as plt

algorithms = []
times = []
nodes = []

with open('results.csv', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        algorithms.append(row['Algorithm'])
        times.append(float(row['Average Time (ms)']))
        nodes.append(int(row['Nodes Expanded']))

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].bar(algorithms, times)
axes[0].set_title('Average Execution Time')
axes[0].set_ylabel('Time (ms)')
axes[1].bar(algorithms, nodes)
axes[1].set_title('Nodes Expanded')
axes[1].set_ylabel('Number of Nodes')
plt.tight_layout()
plt.savefig('performance_graph.png', dpi=200)
plt.show()
print('performance_graph.png created successfully.')