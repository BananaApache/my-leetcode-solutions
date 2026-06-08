class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        pre2courses = { num : [] for num in range(numCourses) }
        for course, pre in prerequisites:
            pre2courses[pre].append(course)

        visited = set()

        def dfs(pre):
            # base cases
            if pre in visited:
                return False
            if pre2courses[pre] == []:
                return True

            visited.add(pre)

            for course in pre2courses[pre]:
                if not dfs(course):
                    return False

            pre2courses[pre] = []
            visited.remove(pre)
            return True

        for pre in pre2courses:
            if not dfs(pre):
                return False
        
        return True


