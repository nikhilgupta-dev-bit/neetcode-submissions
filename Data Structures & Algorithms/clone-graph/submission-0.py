"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque 
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mpp={}
        if not node :
            return None 
        # we need to track nodes and connections 
        mpp[node]=Node(node.val)
        q=deque([node])
        visited=set()
        while q:
            curr=q.popleft()
            visited.add(curr)
            for nei in curr.neighbors :
                if nei not in mpp:
                    # if it not created then only craete it 
                    mpp[nei]=Node(nei.val)
                    q.append(nei)
                mpp[curr].neighbors.append(mpp[nei])
        return mpp[node]


        



