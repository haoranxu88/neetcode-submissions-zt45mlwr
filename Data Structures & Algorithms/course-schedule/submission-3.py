class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = defaultdict(list)
        for course, p in prerequisites:
            pre[course].append(p)
        taken = set()
        taking = set()
        def dfs(course):
            if course in taken:
                return True
            if course in taking:
                return False
            taking.add(course)
            for p in pre[course]:
                if not dfs(p):
                    return False
            taken.add(course)
            taking.remove(course)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True