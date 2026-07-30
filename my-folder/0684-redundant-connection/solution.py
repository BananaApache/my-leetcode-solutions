class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        # union find for connected undirected graph
        # treat edges as [parent, node]
        # on each pair, run find on parent
        # after that, check is parent is equal to root parent
        # that means there is a cycle

        node2parent = { node : node for node in range(1,len(edges)+1) }

        # find a node's super parent (root parent)
        def find(node):
            while node != node2parent[node]: # stop when parent = node2parent[node] (parent is its own parent)
                node = node2parent[node]
            return node
        
        # unioning the pairs
        for n1, n2 in edges:
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return [n1, n2]
            node2parent[p2] = p1

