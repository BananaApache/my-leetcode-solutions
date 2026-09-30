"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']=None) -> Optional['Node']:
        
        # old2new mapping old nodes to newly made nodes
        # can traverse original graph and get all new nodes

        if not node:
            return None

        old2new = {}
        def dfs(node):
            # base case
            if node in old2new:
                return old2new[node]
            
            # we know this is a new node now
            old2new[node] = Node(node.val)

            # we go through the old ones neighbors
            for neighbor in node.neighbors:
                old2new[node].neighbors.append(dfs(neighbor))
            return old2new[node]

        return dfs(node)

