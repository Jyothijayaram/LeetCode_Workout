class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        # finding the missing number bw 1-n
        missing_num = sum( range( len(nums)+1) ) - sum( set(nums) )
        
        # To find the duplicate number in an array 
        dup=[k for k,v in Counter(nums).items() if v > 1]
        
        return *dup,missing_num
        
                
            
    
            
        