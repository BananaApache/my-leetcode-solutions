class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        

        # union find with path compression and also ranking
        parentMap = {node: node for node in range(1, len(edges) + 1)}
        sizeMap = {node: 1 for node in range(1, len(edges) + 1)}

        def find(node):
            # base case
            # path compression part here
            # basically sets each node to its 'root' parent immediately
            if node == parentMap[node]:
                return parentMap[node]
            parentMap[node] = find(parentMap[node])
            return parentMap[node]

        for n1, n2 in edges:
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return [n1, n2]
            else:
                # union part
                if sizeMap[p1] > sizeMap[p2]:
                    # p2 smaller
                    # attach p2 under p1
                    parentMap[p2] = p1
                    sizeMap[p1] += sizeMap[p2]
                else:
                    parentMap[p1] = p2
                    sizeMap[p2] += sizeMap[p1]


        # union find with path compression
        # parentMap = {node: node for node in range(1, len(edges) + 1)}

        # def find(node):
        #     # base case
        #     # path compression part here
        #     # basically sets each node to its 'root' parent immediately
        #     if node == parentMap[node]:
        #         return parentMap[node]
        #     parentMap[node] = find(parentMap[node])
        #     return parentMap[node]

        # for n1, n2 in edges:
        #     p1 = find(n1)
        #     p2 = find(n2)

        #     if p1 == p2:
        #         return [n1, n2]
        #     else:
        #         parentMap[p2] = p1 # union part
        #         # parentMap[p1] = p2 ALSO WORKS, BUT UNION BY RANK OPTIMIZES THIS

        # simple union find implementation
        # parentMap = {node: node for node in range(1, len(edges) + 1)}

        # def find(node):
        #     # base case
        #     if parentMap[node] == node:
        #         return node
            
        #     return find(parentMap[node])
        
        # for n1, n2 in edges:
        #     p1 = find(n1)
        #     p2 = find(n2)

        #     if p1 == p2:
        #         return [n1, n2]
        #     else:
        #         parentMap[p1] = p2

            

