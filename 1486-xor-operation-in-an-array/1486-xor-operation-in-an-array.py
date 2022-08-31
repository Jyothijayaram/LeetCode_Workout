class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        
        # for i in range(n):
        #     start=start ^ (i * 2)
        # return start
        # return reduestart^(i*2) for i in range(n)
        return reduce(operator.xor,[start+(2*i) for i in range(n)])
    
    
    
        
    
            
        
        