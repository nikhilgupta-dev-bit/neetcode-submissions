from collections import deque 
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # we are given is a edge list so forst converted into a graph 
        # 0 based indexing 
        # the graph can be directed one 
        # as the order matters so we can use khan algo 
        reachable = [[False] * numCourses for _ in range(numCourses)]
        for u, v in prerequisites:
            reachable[u][v] = True
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    reachable[i][j] |= (
                        reachable[i][k] and reachable[k][j]
                    )

        return [reachable[u][v] for u, v in queries]
        
        
        