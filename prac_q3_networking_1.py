from collections import defaultdict, deque
import sys

def solve(n, connections):
    # Create a graph
    graph = defaultdict(set)
    for u, v in connections:
        graph[u].add(v)
        graph[v].add(u)
    
    # BFS starting from Server 1
    visited = set()
    queue = deque([1]) # Server 1 is the starting point
    while queue:
        server = queue.popleft()
        if server not in visited:
            visited.add(server)
            queue.extend(graph[server])
    
    # Find and return servers not connected to Server 1
    not_connected = [i for i in range(1, n+1) if i not in visited]
    return not_connected if not_connected else ["All connected"]

all_lines = sys.stdin.readlines()
all_lines = [tuple([int(a) for a in lines.strip().split(" ")]) for lines in all_lines]
N, M = all_lines[0]
links = all_lines[1:]

res = solve(N, links)
for line in res:
    print(line)