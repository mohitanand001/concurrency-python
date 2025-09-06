import pytest
from collections import deque

def bfs(graph, start):
    """Breadth-First Search implementation."""
    visited = []
    queue = deque([start])
    seen = set([start])
    
    while queue:
        node = queue.popleft()
        visited.append(node)

        print(node)
        for neighbor in graph.get(node, []):
            if neighbor not in seen:
                queue.append(neighbor)
                seen.add(neighbor)
    
    return visited

