class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        course2pre = defaultdict(list)

        for course, pre in prerequisites:
            course2pre[course].append(pre)

        visited = set()
        def dfs(course):
            # base cases
            if course in visited:
                return False
            if course2pre[course] == []:
                return True
            
            visited.add(course)
            for pre in course2pre[course]:
                if not dfs(pre):
                    return False
            
            visited.remove(course)
            course2pre[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True


