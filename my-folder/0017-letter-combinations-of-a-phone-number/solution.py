class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        hashmap = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }

        result = []
        def dfs(index, comb):
            # base case
            if index >= len(digits):
                result.append(comb)
                return
            
            for char in hashmap[digits[index]]:
                dfs(index + 1, comb + char)
        
        dfs(0, "")
        return result

