class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic={}
        counter=0
        for num in nums:
            if num in dic:
                counter+=dic[num]
                dic[num]+=1
            else:
                dic[num]=1
        return counter
        
        


        