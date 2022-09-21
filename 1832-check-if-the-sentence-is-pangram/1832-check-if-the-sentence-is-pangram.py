class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        h={}
        
        for c in sentence:
            if c not in h: 
                h[c]=1
        return sum(h.values())==26
         
#         else:
#             return False
        