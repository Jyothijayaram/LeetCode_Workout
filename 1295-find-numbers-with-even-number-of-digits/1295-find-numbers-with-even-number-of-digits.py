class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even=0
        def evn(num):
            count=0
            while num>0:
                count+=1
                num=num//10
            return count
        for n in nums:
            if evn(n) % 2==0:
                even+=1
        return even
        