class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        large=0
        for p in accounts:
            large=max(sum(p), large)
        return large