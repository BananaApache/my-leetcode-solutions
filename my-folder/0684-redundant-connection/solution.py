class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        adjMap = { node : set() for node in range(1, len(edges) + 1) }
        for a, b in edges:
            adjMap[a].add(b)
            adjMap[b].add(a)
        
        visited = set()
        cycle = set()
        cycleStart = None
        cycleClosed = False

        def isCycle(node, prev):
            nonlocal cycleStart, cycleClosed
            # base case
            if node in visited:
                cycleStart = node
                return True
            
            visited.add(node)
            for neighbor in adjMap[node]:
                if neighbor != prev and isCycle(neighbor, node):
                    if not cycleClosed:
                        cycle.add((node, neighbor))
                        if node == cycleStart:
                            cycleClosed = True

                    return True
            
            return False

        isCycle(1, -1)

        for index in range(len(edges) - 1, -1, -1):
            a, b = edges[index]

            if (a, b) in cycle or (b, a) in cycle:
                return [a, b]

