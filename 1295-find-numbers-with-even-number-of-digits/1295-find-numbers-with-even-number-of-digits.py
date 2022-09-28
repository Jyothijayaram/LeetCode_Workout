class Solution:
    import math
    def findNumbers(self, nums: List[int]) -> int:
        
        count=0    
        for i in nums:
            if int(math.log10(i)+1) % 2==0:         
#         To Count the Number of digits in nums
                count+=1
        return count