class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:

        adj = [[] for i in range(numCourses)]
        indegree = [0]*numCourses
        res = []
        for i,j in prerequisites:
            adj[j].append(i)
            indegree[i] += 1

        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()
            res.append(node)

            for neigh in adj[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
        print(res)
        if len(res) != numCourses:
            return []
        
        return res