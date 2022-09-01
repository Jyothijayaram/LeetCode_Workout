class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res=str(s+t)
        ans=0
        for letter in res:
            ans=ans ^ ord(letter)
            
        return chr(ans)
        
       
                
       