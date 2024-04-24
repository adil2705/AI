
from collections import defaultdict

def bfs(graph, start, goal):
    visited = set()
    queue = [[start]]
    
    while queue:
        path = queue.pop(0)
        node = path[-1]
        
        if node == goal:
            return path
        
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                new_path = path + [neighbor]  # Create a new path for each neighbor
                queue.append(new_path)
    
    return []

def dfs(graph, start, goal):
    visited = set()
    stack = [[start]]
    
    while stack:
        path = stack.pop()
        node = path[-1]
        
        if node == goal:
            return path
        
        if node not in visited:
            visited.add(node)
            for neighbor in reversed(graph[node]):
                new_path = path + [neighbor]  # Create a new path for each neighbor
                stack.append(new_path)
    
    return []

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

start_node = 'A'
goal_node = 'F'

bfs_path = bfs(graph, start_node, goal_node)
dfs_path = dfs(graph, start_node, goal_node)

print("BFS Path:", "->".join(bfs_path))
print("DFS Path:", "->".join(dfs_path))
