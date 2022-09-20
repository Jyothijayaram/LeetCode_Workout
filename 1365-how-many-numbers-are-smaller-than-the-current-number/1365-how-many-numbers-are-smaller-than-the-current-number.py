class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        h={}
        def smaller(ele):
            count=0
            for n in nums:
                if n < ele:
                    count+=1
            return count
        for ele in nums:
            if ele in h:
                continue
            else:
                h[ele]=smaller(ele)
        return [h[i] for i in nums]
        