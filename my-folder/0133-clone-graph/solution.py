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
        
        if not node:
            return None

        old2new = {}

        old2new[node] = Node(node.val)
        q = deque([node])

        while q:
            newNode = q.popleft()
            
            for neighbor in newNode.neighbors:
                if neighbor not in old2new:
                    old2new[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                old2new[newNode].neighbors.append(old2new[neighbor])

        return old2new[node]

