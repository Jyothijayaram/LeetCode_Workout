class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s=set(nums)
        high=0
        count=0
        for ele in s:
            count=0
            for j in range(0,len(nums)):
                if ele==nums[j]:
                    count+=1
            if count>high:
                max_ele=ele
                high=count
        return max_ele
                    
            
        