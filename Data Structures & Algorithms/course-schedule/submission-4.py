class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create graph with hashmap
        prereqs = defaultdict(list)
        for p, c in prerequisites:
            prereqs[c].append(p)
        # we want to detect cycle
        seen = set()
        current = set()
        def dfs(course):
            if course in seen:
                return True
            if course in current:
                return False
            current.add(course)
            for pre in prereqs[course]:
                if not dfs(pre):
                    return False
            current.remove(course)
            seen.add(course)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

