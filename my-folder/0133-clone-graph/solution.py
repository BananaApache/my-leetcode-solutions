"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if node is None:
            return None

        old2new = {}

        def bfs(start):
            q = deque([start])
            old2new.update( {start : Node(start.val)} )

            while q:
                node = q.popleft()
                for neighbor in node.neighbors:
                    if neighbor not in old2new:
                        q.append(neighbor)
                        old2new[neighbor] = Node(neighbor.val)
                        
                    old2new[node].neighbors.append(old2new[neighbor])

        bfs(node)
        
        return old2new[node]


