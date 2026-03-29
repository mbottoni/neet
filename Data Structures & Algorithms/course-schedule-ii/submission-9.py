class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build adj matrix
        d={}
        for course in range(numCourses):
            d[course] = []
        for course, pre in prerequisites:
            d[course] = d[course] + [pre]
        # O(2n)
        
        # find d[course] == []
        # Do the course and go to next d[course] == []
        # if dict is empty at the end return True
        # Else False

        courses = []
        for _ in range(numCourses):
            sorted_dict = {k: v for k, v in sorted(d.items(), key=lambda item: len(item[1]))}
            course = list(sorted_dict.keys())[0]
            if len(d[course])==0:
                courses.append(course)
                del d[course]
                # Remove from prereqs
                for keys in d:
                    prereq = d[keys]
                    # remove the course from prereq arrays
                    if course in prereq:
                        prereq.remove(course)
                    d[keys] = prereq
            else:
                return []


        return courses
        