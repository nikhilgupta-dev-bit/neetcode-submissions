from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # i have been give with edge list 
        # graph 
        # this is eulirian circuit problem 
        # we vivsit each edge is vivited once 
        #. An Euler circuit is a path that traverses every edge of a graph exactly once, and the path ends on the starting vertex.
        #All vertices belong to a single strongly connected component. (2) All vertices have same in-degree and out-degree. Note that for an undirected graph, the condition is different (all vertices have even degree)
        # This is Hierholzer's Algorithm for directed graph
        graph = defaultdict(list)
        # reverse sort so smallest lexical airport can be popped last
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)
        itinerary = []
        def dfs(airport):
            while graph[airport]:
                nxt = graph[airport].pop()
                dfs(nxt)
            itinerary.append(airport)
        dfs("JFK")
        return itinerary[::-1]