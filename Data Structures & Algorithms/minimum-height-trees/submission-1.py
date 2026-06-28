from collections import deque 
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # we have to find the middle of graph that will give us minimum height 
        # base case 
        if n==1:
            return [0]
        # s-1 create the graph 
        graph=defaultdict(list)
        degree=[0]*n
        for u,v in edges :
            graph[u].append(v)
            graph[v].append(u)
            degree[u]+=1
            degree[v]+=1
        q=deque()
        visited=set()
        # push all the nodes with degree 1 on it and then we keep on pop it 
        for i in range(n):
            if degree[i]==1:
                visited.add(i)
                q.append(i)
        remaining=n 
        # BFS 
        while remaining>2:
            size=len(q)
            remaining-=size
            for _ in range(size):
                leaf=q.popleft()
                for nei in graph[leaf]:
                    degree[nei]-=1
                    if degree[nei]==1 and nei not in visited:
                        visited.add(nei)
                        q.append(nei)
        return list(q)

        
