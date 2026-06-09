class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        course2pres = { course : [] for course in range(numCourses) }
        for course, pre in prerequisites:
            course2pres[course].append(pre)

        result = []
        visited = set()
        inResult = set()
        
        def dfs(course):
            # base cases
            if course in visited:
                return False # cycle detected
            if course2pres[course] == []:
                if course not in inResult:
                    result.append(course)
                    inResult.add(course)
                return True # found course with no prereqs

            visited.add(course)
            for pre in course2pres[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            course2pres[course] = []
            result.append(course)
            inResult.add(course)

            return True

        for course in course2pres:
            if not dfs(course):
                return []

        return result

