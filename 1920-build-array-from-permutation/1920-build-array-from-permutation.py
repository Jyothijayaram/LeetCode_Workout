class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans= []
        for index in range(0,len(nums)):
            ans.append(nums[nums[index]])
        return ans
        