class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        
        # course 2 pres
        course2pres = { course: [] for course in range(numCourses) }
        for course, pre in prerequisites:
            course2pres[course].append(pre)

        # add a course to finished result once we took all prerequisites
        # can be tracked with value of [] in course2pres map
        # can also keep track of which is already appended with some set
        # can use set cycle to keep track of current cycle and detect cycles

        result = []
        currCycle = set()
        seen = set()

        def dfs(course):
            # base case
            if course in currCycle: # we found a cycle
                return False
            if course in seen:
                return True
            
            currCycle.add(course) # add current course to our current Cycle
            # go through that courses pres
            for pre in course2pres[course]:
                if not dfs(pre): # stop if we found cycle
                    return False
            # we didnt find any cycles, took all pres
            currCycle.remove(course)
            course2pres[course] = []
            result.append(course)
            seen.add(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return result
