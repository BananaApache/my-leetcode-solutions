class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        course2pre = defaultdict(list)
        for course, pre in prerequisites:
            course2pre[course].append(pre)
        
        seen = set()
        cycle = set()
        result = []

        def dfs(course):
            # base case
            if course in seen: # equal to course2pre[course] == []
                return True
            if course in cycle:
                return False

            cycle.add(course)
            for pre in course2pre[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)

            seen.add(course)
            result.append(course)

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
            
        return result

