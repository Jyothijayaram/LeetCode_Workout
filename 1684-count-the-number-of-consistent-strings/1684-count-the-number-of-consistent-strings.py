class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        for word in words:
            for i in range(0,len(word)):
                if word[i] not in allowed:
                    count-=1
                    break
            count+=1
        return count
       
                
        