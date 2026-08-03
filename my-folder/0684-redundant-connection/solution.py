class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parentMap = { node : node for node in range(1,len(edges)+1) }
 
        # find function with halving path compression
        # def find(node):
        #     # will find a nodes root parent
        #     while node != parentMap[node]:
        #         parentMap[node] = parentMap[parentMap[node]] # sets a node parent to its grandparent
        #         node = parentMap[node]
        #     return node

        # find function with recursive path compression
        def find(node):
            # base case
            if parentMap[node] == node:
                return node

            parentMap[node] = find(parentMap[node])
            return parentMap[node]

        # union part
        for node1, node2 in edges:
            parent1, parent2 = find(node1), find(node2)

            if parent1 == parent2:
                return [node1, node2]
            else:
                parentMap[parent2] = parent1

