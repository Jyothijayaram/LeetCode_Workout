class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start=0
        end=len(letters)-1
        mid=(start+end)//2
        while(start<=end):
            if target>=letters[mid]:
                start=mid+1
                mid=(start+end)//2
            else:
                end=mid-1
                mid=(start+end)//2
        return letters[start % len(letters)]