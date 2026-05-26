class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        hashmap = [
            (), 
            (), 
            ('a','b','c'),
            ('d','e','f'),
            ('g','h','i'),
            ('j','k','l'),
            ('m','n','o'),
            ('p','q','r','s'),
            ('t','u','v'),
            ('w','x','y','z')
        ]

        result = []

        def backtrack(node, index):
            # base case
            if index == len(digits):
                result.append(node)
                return
            
            for char in hashmap[int(digits[index])]:
                backtrack(node + char, index + 1)
        
        backtrack("", 0)

        return result

