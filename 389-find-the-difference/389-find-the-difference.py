class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sum=0
        sum2=0
        for letter in s:
            sum=sum+ord(letter)
        for letter2 in t:
            sum2=sum2+ord(letter2)
        return chr(sum2-sum)
        
       
                
       