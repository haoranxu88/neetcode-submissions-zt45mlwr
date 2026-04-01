class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre = defaultdict(list)
        for course, p in prerequisites:
            pre[course].append(p)
        taken = set()
        taking = set()
        res = []
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
            res.append(course)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res