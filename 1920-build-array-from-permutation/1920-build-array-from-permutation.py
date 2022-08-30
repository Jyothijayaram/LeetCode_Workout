class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)
        for index in range(0,len(nums)):
            ans[index]=nums[nums[index]]
        return ans
        