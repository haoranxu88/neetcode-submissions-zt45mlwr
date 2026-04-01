class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preqs = defaultdict(list)
        for a, b in prerequisites:
            preqs[a].append(b)
        taken = set()
        taking = set()
        def dfs(course):
            if course in taken:
                return True #verified part of a non-cyclic path
            if course in taking:
                return False #cycle detected 
            taking.add(course)
            for p in preqs[course]:
                if not dfs(p):
                    return False
            taking.remove(course)
            taken.add(course)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

        