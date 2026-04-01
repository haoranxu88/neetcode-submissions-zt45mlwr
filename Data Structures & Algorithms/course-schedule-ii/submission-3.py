class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preqs = defaultdict(list)
        for c, p in prerequisites:
            preqs[c].append(p)
        taken = set()
        taking = set()
        res = []
        def dfs(course):
            if course in taken:
                return True
            if course in taking:
                return False
            taking.add(course)
            for p in preqs[course]:
                if not dfs(p):
                    return False
            taken.add(course)
            taking.remove(course)
            res.append(course)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return []
        return res