class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preqs = defaultdict(list)
        for a, b in prerequisites:
            preqs[a].append(b)
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
            res.append(course)
            taken.add(course)
            taking.remove(course)
            return True
        for n in range(numCourses):
            if not dfs(n):
                return []
        return res