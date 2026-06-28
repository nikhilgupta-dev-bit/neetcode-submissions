from collections import defaultdict, deque
from typing import List
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # so this  can be done in three ways 
        # 1. weighted BFS (joh abhi karuga ) 
        # 2. DSU+ weights 
        # 3. Floyd washeel algo relationship btw each node 
        # the imp is to establish a relationship btw a,b,c and then its just multiplication 
        # return type should be floor 
        graph = defaultdict(list)
        # Build weighted graph
        for (u, v), val in zip(equations, values):
            graph[u].append((v, val))
            graph[v].append((u, 1 / val))
        def bfs(src,dst):
            if src not in graph or dst not in graph :
                return -1.0
            if src==dst:
                # we have a , b, c ,d hence 1 will be returned 
                return 1.0 
            # what are we gonna store in q=> (node,product) src/node
            q=deque([(src,1.0)])
            visited=set()
            visited.add(src)
            while q:
                node,product= q.popleft()
                if node==dst:
                    return product 
                for nei,wt in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei,product*wt))
            return -1.0 
        ans=[]
        for src,dst in queries:
            ans.append(bfs(src,dst))
        return ans 
                







