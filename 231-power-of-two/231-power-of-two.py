class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n > 0:
            while not (n & 1) or n==1:
                if n==1:
                    return True
                n=n//2
        return False
        
        
                
        