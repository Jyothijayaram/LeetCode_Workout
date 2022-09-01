class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        # finding the missing number bw 1-n
        missing_num = sum( range( len(nums)+1) ) - sum( set(nums) )
        
        # To find the duplicate number in an array 
        dup = sum(nums) - sum(set(nums))


        
        return dup,missing_num
        
                
            
    
            
        