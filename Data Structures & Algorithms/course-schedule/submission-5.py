class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preqs = defaultdict(list)
        for p, c in prerequisites:
            preqs[c].append(p)
        taken = set()
        taking = set()
        def dfs(course):
            if course in taken:
                return True
            if course in taking:
                return False
            taking.add(course)
            for p in preqs[course]:
                if not dfs(p):
                    return False
            taking.remove(course)
            taken.add(course)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True