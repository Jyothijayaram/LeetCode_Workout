class Solution:
    def countBits(self, n: int) -> List[int]:
        result=[]
        for i in range(n+1):
            cnt=0
            while i>0:
                if i & 1:
                    cnt+=1
                i=i>>1
            result.append(cnt)
        return result 
        