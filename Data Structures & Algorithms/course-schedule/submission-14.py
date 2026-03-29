class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            d[course].append(prereq)
        
        cond = []
        def visit_courses(course):
            if course in vis:
                cond.append(False)
                return 
            else:
                vis.add(course)

            if d[course] == []:
                cond.append(True)

            for pre in d[course]:
                visit_courses(pre)
                
            vis.remove(course)

        vis = set()
        for course in range(numCourses):
            visit_courses(course)

        return all(cond)
