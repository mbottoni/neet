class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = {i: [] for i in range(numCourses)}
        # Build adj matrix
        for pre in prerequisites:
            d[pre[0]] = d[pre[0]]+[pre[1]]
        
        while d:
            d = {k: v for k,v in sorted(d.items(), key=lambda item: len(item[1]))} # sort by n prereq
            course = list(d.keys())[0]
            if len(d[course])==0:
                for c in range(numCourses):
                    if c in d and course in d[c]:
                        d[c].remove(course)
                del d[course]
            else:
                break

        return True if d=={} else False