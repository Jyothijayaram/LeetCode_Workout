class Solution:
    def numberOfSteps(self, num: int) -> int:
        bin_num_len=bin(num)[2:]
        return len(bin_num_len)-1+bin_num_len.count('1')
        
        
    
        