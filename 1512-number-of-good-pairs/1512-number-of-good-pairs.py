class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic={}
        counter=0
        for num in nums:
            if num in dic:
                # counter+=dic[num]
                dic[num]+=1
            else:
                dic[num]=1
        for val in dic.values():
            counter=counter + (val * (val-1)) // 2
        return counter
       
        
        


        