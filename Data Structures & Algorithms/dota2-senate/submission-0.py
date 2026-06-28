class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        s=list(senate)
        r_ban=0 
        d_ban=0 
        while True :
            new_s=[]
            for ch in s:
                if ch=='R':
                    if r_ban>0:
                        r_ban-=1
                    else :
                        d_ban+=1
                        new_s.append('R')
                else :
                    if d_ban>0:
                        d_ban-=1
                    else:
                        r_ban+=1
                        new_s.append('D')
              # check if one party is gone
            if all(c == 'R' for c in new_s):
                return "Radiant"
            if all(c == 'D' for c in new_s):
                return "Dire"
            
            s = new_s





