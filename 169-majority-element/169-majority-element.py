class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic={}
        for ele in nums:
            if ele not in dic:
                dic[ele]=nums.count(ele)
        return max(dic,key=dic.get)
        
                    
            
        