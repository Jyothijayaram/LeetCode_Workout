class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        lst_int = int("".join(map(str,num)))
        return list(str(lst_int+k))
        