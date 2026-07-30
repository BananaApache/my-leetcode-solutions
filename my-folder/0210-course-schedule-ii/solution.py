class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # node represents one course
        # edge represents that node's required courses. course -> pre
        # need to find courses to take before current course in order

        # dfs: go down all prereqs until finding a good one, then take that and go back up
        # recurrence: add course to output once all prereqs are taken

        course2pre = defaultdict(list)
        for course, pre in prerequisites:
            course2pre[course].append(pre)

        output = []
        taken = set()
        cycle = set()
        def dfs(course):
            # base case
            if course in cycle:
                return False
            if course in taken:
                return True
            
            cycle.add(course)
            for pre in course2pre[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)

            taken.add(course)
            output.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return output

