class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            d[course].append(prereq)

        VISITING, VISITED = 1, 2
        state = {}

        def has_cycle(course):
            if state.get(course) == VISITING:
                return True
            if state.get(course) == VISITED:
                return False
            state[course] = VISITING
            if any(has_cycle(pre) for pre in d[course]):
                return True
            state[course] = VISITED
            return False

        return not any(has_cycle(c) for c in range(numCourses))