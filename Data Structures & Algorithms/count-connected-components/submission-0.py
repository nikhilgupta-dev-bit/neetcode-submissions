class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # this is a dsu 
        # 0 based indexing 
        class DSU :
            def __init__(self,n):
                self.parent=[ i for i in range(n)]
                self.rank=[0]*n
            def find(self,node):
                if node==self.parent[node]:
                    return node 
                self.parent[node]=self.find(self.parent[node])
                return self.parent[node]
            def union(self,a,b):
                pa=self.find(a)
                pb=self.find(b)
                if pa==pb:
                    return False 
                if self.rank[pa]>self.rank[pb]:
                    self.parent[pb]=pa
                elif self.rank[pb]>self.rank[pa]:
                    self.parent[pa]=pb
                else :
                    self.parent[pa]=pb
                    self.rank[pb]+=1
                return True 
        no_of_components=n
        uf=DSU(n)
        for u,v in edges:
            if uf.union(u,v):
                no_of_components-=1
        return no_of_components

            
            



