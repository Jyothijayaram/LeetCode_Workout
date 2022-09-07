class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        cnt=0
        while n>0:
            if n & 1 ==1:
                cnt+=1
            n=n>>1
        if cnt ==1 :
            return True
        else:
            return False
        
        
        
        
        
        
        
                
        