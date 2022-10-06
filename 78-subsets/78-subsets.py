class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
#         Brute Force Approch
        output=[[]]
        for i in nums:
            output+=[ n + [i] for n in output]
        return output
            