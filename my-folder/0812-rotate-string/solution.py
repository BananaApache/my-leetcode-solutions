class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        if len(s) != len(goal):
            return False
        
        length = len(s)
        for index in range(length):
            if s[index:] == goal:
                return True
            
            s += s[index]

        return False
        
