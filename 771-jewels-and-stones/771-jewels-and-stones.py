class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dic={}
        for s in stones:
            if s in stones and s in jewels:
                if s in dic:
                    dic[s]+=1
                else:
                    dic[s]=1
        return sum(dic.values())
            