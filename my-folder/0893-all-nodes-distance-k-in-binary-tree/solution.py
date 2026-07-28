# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        adjMap = defaultdict(list)

        q = deque([root])
        while q:
            node = q.popleft()

            if node.left:
                adjMap[node.val].append(node.left.val)
                adjMap[node.left.val].append(node.val)
                q.append(node.left)
            if node.right:
                adjMap[node.val].append(node.right.val)
                adjMap[node.right.val].append(node.val)
                q.append(node.right)
        
        result = []

        q = deque([(target.val, 0)]) # ( node, distance from target )
        seen = set([target.val])
        while q:
            node, distance = q.popleft()
            if distance == k:
                result.append(node)
                continue

            for neighbor in adjMap[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    q.append( (neighbor, distance + 1) )
            
        return result

