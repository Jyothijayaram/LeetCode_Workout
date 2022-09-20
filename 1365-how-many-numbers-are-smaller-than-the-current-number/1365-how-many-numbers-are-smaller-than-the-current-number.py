class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sor_arr=sorted(nums)
        return [sor_arr.index(i) for i in nums ]
            
        
        