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

        q = deque([node])
        while q:
            oldNode = q.popleft()
            if oldNode not in old2new:
                old2new[oldNode] = Node(oldNode.val)

            for oldNeighbor in oldNode.neighbors:
                if oldNeighbor not in old2new:
                    old2new[oldNeighbor] = Node(oldNeighbor.val)
                    q.append(oldNeighbor)
                old2new[oldNode].neighbors.append(old2new[oldNeighbor])

        return old2new[node]

