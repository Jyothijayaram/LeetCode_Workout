class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums) # find the no of elements in list
        return int((n+1)/2 * n-sum(nums))
        
        