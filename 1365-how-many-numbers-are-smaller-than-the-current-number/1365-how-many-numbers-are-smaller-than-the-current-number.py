class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sor_arr=sorted(nums)
        res=[]
        for i in nums:
            res.append(sor_arr.index(i))
        return res
            
        
        