class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegrees = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a) # b -> a
            indegrees[a] += 1

        q = deque()
        for i, indegree in enumerate(indegrees):
            if indegree == 0:
                q.append(i)

        res = []

        while q:
            for _ in range(len(q)):
                course = q.popleft()
                res.append(course)
                for neighbor in graph[course]:
                    indegrees[neighbor] -= 1
                    if indegrees[neighbor] == 0:
                        q.append(neighbor)

        if len(indegrees) != len(res):
            return []

        return res
