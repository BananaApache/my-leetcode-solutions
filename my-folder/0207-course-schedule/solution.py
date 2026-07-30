class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # directed, could be unconnected components
        # all nodes represent courses
        # edges can represents this course needs its neighbor courses. course -> pre
        # a cycle means it is impossible to take all courses
        # detecting cycle return False
        # dfs is more natural at detecting cycles

        # dfs() will answer if this course can be completed or not, or false if there is cycle
        # recurrence: return whether or not all my neighor courses can be taken

        course2pres = { course : [] for course in range(numCourses) }
        for course, pre in prerequisites:
            course2pres[course].append(pre)
        
        cycle = set()
        def dfs(course):
            # base case
            if course in cycle:
                cycle.remove(course)
                return False

            cycle.add(course)
            for pre in course2pres[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)
            course2pres[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True

