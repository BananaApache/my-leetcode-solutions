# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # dfs(root): traverses down and appends root, left, right to output

        def dfs(root):
            # base case
            if not root:
                return 'n,'
            
            return str(root.val) + "," + dfs(root.left) + dfs(root.right)
        return dfs(root)[:-1]

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # dfs(): goes through data incrementing index while build tree

        data = data.split(",")
        index = 0
        def dfs():
            nonlocal index

            # base case
            if data[index] == "n" or index >= len(data):
                return None

            root = TreeNode(int(data[index]))
            index += 1
            root.left = dfs()
            index += 1
            root.right = dfs()

            return root
        
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
