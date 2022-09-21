class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        character= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for c in character:
            if c in sentence:
                continue
            else:
                return 0
        return 1
                
        