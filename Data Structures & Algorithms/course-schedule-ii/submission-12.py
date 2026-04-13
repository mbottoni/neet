class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d = {i: [] for i in range(numCourses)}
        # Build adj matrix
        for pre in prerequisites:
            d[pre[0]] = d[pre[0]]+[pre[1]]
        
        order = []
        while d:
            d = {k: v for k,v in sorted(d.items(), key=lambda item: len(item[1]))} # sort by n prereq
            course = list(d.keys())[0]
            if len(d[course])==0:
                order.append(course)
                for c in range(numCourses):
                    if c in d and course in d[c]:
                        d[c].remove(course)
                del d[course]
            else:
                break

        if len(order)==numCourses:
            return order
        return []
        