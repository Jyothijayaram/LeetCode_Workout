class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m=-1
        counter=0
        for i in range(len(nums)):
            if counter==0:
                m=nums[i]
                counter=1
            elif nums[i]==m:
                counter+=1
            else:
                counter-=1
        return m
        
        
       
            
        