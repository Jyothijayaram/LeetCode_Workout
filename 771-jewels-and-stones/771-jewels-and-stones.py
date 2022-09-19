class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dic={}
        c=0
        for s in stones:
         
                if s in dic:
                    dic[s]+=1
                else:
                    dic[s]=1
        for k in dic:
            if k in jewels:
                c=c+dic[k]
        return c
            