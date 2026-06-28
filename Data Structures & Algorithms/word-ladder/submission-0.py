from collections import deque, defaultdict
from typing import List
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # the diffrence between the words should be one 
        # we will use a wild card at a index and change it one by one permutations to get endword 
        if endWord not in wordList:
            return 0
        combinations=defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                tmp=word[:i]+"*"+word[i+1:]
                combinations[tmp].append(word)
        # this will create permuations for every  word like 
        #defaultdict(<class 'list'>, {'*ot': ['hot', 'dot', 'lot'], 'h*t': ['hot'], 'ho*': ['hot'], 'd*t': ['dot'], 'do*': ['dot', 'dog'], '*og': ['dog', 'log', 'cog'], 'd*g': ['dog'], 'l*t': ['lot'], 'lo*': ['lot', 'log'], 'l*g': ['log'], 'c*g': ['cog'], 'co*': ['cog']})
        # now we can run a bfs 
        # start node and first word 
        q=deque([(beginWord,1)])
        visited=set()# visited array isliye bana rha hain so that we dont have a cycle
        visited.add(beginWord)
        while q :
            curr,level=q.popleft()
            if curr==endWord:
                return level
            for i in range(len(curr)):
                temp=curr[:i]+"*"+curr[i+1:]
                for w in combinations[temp]:
                    if w not in visited:
                        visited.add(w)
                        q.append((w,level+1))
        return 0 





            




