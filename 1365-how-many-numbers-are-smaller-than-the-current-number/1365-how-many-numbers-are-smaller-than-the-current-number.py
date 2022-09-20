class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        orignal_arr=[i for i in nums]
        nums.sort()
        return [nums.index(i) for i in orignal_arr ]
            
        
        