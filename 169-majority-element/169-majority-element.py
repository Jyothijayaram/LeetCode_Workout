class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic={}
        for ele in nums:
            dic[ele]=dic.get(ele,0)+1
            
        for key,val in dic.items():
            if val > len(nums)//2:
                return key
        
       
            
        