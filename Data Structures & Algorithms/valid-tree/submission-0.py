from collections import deque 
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # bfs 
        # we have to create a graph it is given in the form of a edge list 
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        q=deque([0])
        visited=set()
        # we start from 0
        visited.add(0)
        # this is a tree definatiom 
        if len(edges)!=n-1:
            return False 
        while q :
            node=q.popleft()
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)
        # if all the nodes are added and edges are equal to n then its a cycle 
        return len(visited)==n





