class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        for count in range(0,k):
            nums.insert(0,nums.pop())
        """
        Do not return anything, modify nums in-place instead.
        """
        