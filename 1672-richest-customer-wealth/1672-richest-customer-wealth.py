class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi=0
        for customer in accounts:
            ans=0
            for wealth in customer:
                ans=ans+wealth
            if ans>maxi:
                maxi=ans
        return maxi