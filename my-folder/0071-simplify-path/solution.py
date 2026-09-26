class Solution:
    def simplifyPath(self, path: str) -> str:
        
        # this pattern of going back up or going to the left sounds like stack
        # each element in the stack is a directory
        # i push when its a valid path
        # i can pop when its '..'
        # ignore everything else

        stack = []
        path = path.split("/")

        for directory in path:
            
            # ignoring cases "" and "."
            if directory == "" or directory == ".":
                continue
            # ".." case
            elif directory == "..":
                if stack:
                    stack.pop()
            # actual directory case
            else:
                stack.append(directory)
        
        return "/" + "/".join(stack)

