class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []

        def dfs(s, left, right):
            # base case
            if left == n == right:
                result.append(s)
                return
            
            if left != right:
                dfs(s + ")", left, right + 1)
            if left != n:
                dfs(s + "(", left + 1, right)

        dfs("(", 1, 0)

        return result

