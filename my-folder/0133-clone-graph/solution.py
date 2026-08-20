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
        
        # can keep a map of old nodes to new nodes
        # go through each node and its neighbors and connect them
        # can use bfs to go through each neighbor

        if not node:
            return None

        old2new = {}

        q = deque([node])
        while q:
            curr = q.popleft()
            if curr not in old2new:
                old2new[curr] = Node(curr.val)

            for neighbor in curr.neighbors:
                if neighbor not in old2new:
                    old2new[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                old2new[curr].neighbors.append(old2new[neighbor])
                
        return old2new[node]

