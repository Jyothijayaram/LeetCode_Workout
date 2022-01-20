class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        S, A = set(), []
        for n in nums:
            if n in S: 
                A.append(n)
            else: 
                S.add(n)
        return A
        
        