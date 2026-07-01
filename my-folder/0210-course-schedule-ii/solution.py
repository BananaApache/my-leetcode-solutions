class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # build adj map
        course2pres = {course : [] for course in range(numCourses)}
        for course, pre in prerequisites:
            course2pres[course].append(pre)

        result = []
        seen = set()
        cycle = set()
        def dfs(course):
            # base case
            if course in seen:
                return True
            if course in cycle:
                return False

            if course2pres[course] == []:
                result.append(course)
                seen.add(course)
                return True

            cycle.add(course)
            for pre in course2pres[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)

            result.append(course)
            seen.add(course)
            
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return result
        

