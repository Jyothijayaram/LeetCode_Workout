class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        uni_sorted=sorted(set(arr))
        dic=dict()
        
        for index,val in enumerate(uni_sorted):
            dic[val] =index +1
        return  [dic[num] for num in arr]