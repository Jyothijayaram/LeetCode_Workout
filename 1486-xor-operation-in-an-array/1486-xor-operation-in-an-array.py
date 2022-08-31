class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans=0
        while n!=0:
            ans=ans ^ start
            n-=1
            start+=2
        return ans
    
        
    
            
        
        