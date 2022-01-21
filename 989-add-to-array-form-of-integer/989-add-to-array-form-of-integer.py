class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        lst_int = int("".join(map(str,num)))
        return [int(n) for n in str(lst_int+k)] # adding k->int->str->each digit(int)->list
        