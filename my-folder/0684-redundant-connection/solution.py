class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parentMap = { node : node for node in range(1, len(edges) + 1) }

        # find parent only
        def find(node):
            # while node != parentMap[node]:
            #     node = parentMap[node]
            
            # return node
            if node != parentMap[node]:
                node = find(parentMap[node])
            return parentMap[node]

        for a, b in edges:
            
            rootParenta = find(a)
            rootParentb = find(b)
            if rootParenta == rootParentb:
                return [a, b]
            else:
                parentMap[rootParentb] = rootParenta

