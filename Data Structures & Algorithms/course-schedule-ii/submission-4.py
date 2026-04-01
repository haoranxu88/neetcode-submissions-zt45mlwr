class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preqs = defaultdict(list)
        for a, b in prerequisites:
            preqs[a].append(b)
        taking = set()
        taken = set()
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
            taking.remove(course)
            taken.add(course)
            res.append(course)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return []
        return res