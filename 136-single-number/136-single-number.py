class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        import functools as f
        return f.reduce(lambda a,b: a^b ,nums)
            
        