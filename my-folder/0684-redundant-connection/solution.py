class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        
        # basic union find, no path compression, no ranking

        parentMap = { edge : edge for edge in range(1, len(edges)+1)}

        def find(node):
            if node == parentMap[node]: # base case: is its parent
                return node
            else:
                parentMap[node] = find(parentMap[node])
                return parentMap[node]
        
        # union part
        for a, b in edges:
            aParent = find(a)
            bParent = find(b)

            if aParent == bParent:
                return [a, b]
            else:
                parentMap[bParent] = aParent

