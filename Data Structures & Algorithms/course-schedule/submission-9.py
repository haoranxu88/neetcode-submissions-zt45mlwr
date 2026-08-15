class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(list)
        for a, b in prerequisites:
            prereqs[a].append(b)
        taking = set()
        taken = set()
        def dfs(course):
            if course in taken:
                return True
            if course in taking:
                return False
            taking.add(course)
            for p in prereqs[course]:
                if not dfs(p):
                    return False
            taking.remove(course)
            taken.add(course)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True