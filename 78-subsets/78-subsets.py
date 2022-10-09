class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]
        def helper(nums,index,res):
            if index==n:
                ans.append(res)
                return
            helper(nums,index+1,res+[nums[index]])
            helper(nums,index+1,res)
        helper(nums,0,[])
        return ans
       