class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # [a, b] : take b -> take a
        # [course, prerequisite]

        # can make adjacencyMap from course to its prerequisites

        course2pre = defaultdict(list)
        for course, pre in prerequisites:
            course2pre[course].append(pre)

        # dfs: keeps traversing until found False. will be True when course has no prerequisities, or finished all of its prerequisities

        cycle = set()
        def dfs(course):
            # base case
            if course in cycle: # cycled course
                return False
            if course2pre[course] == []: # finished course
                return True
            
            cycle.add(course)
            for pre in course2pre[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)
            course2pre[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
