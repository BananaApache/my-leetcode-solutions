class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        # Which edge is the first one that connects two nodes that were already connected?

        
        # find parent of n1, parent of n2
        # both are different -> merge
        # both are same -> found a redundant connection
        # 

        parentMap = { node : node for node in range(1, len(edges)+1) }

        # find: what is this nodes root parent
        def find(node):
            # stop when node is its own parent
            while node != parentMap[node]:
                node = parentMap[node]
            return node

        for n1, n2 in edges:
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return [n1, n2]
            else:
                parentMap[p2] = p1

