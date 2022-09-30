class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start=0
        end=len(arr)-1
        while start<=end:
            mid=(start+end)//2
            if arr[mid-1]<=arr[mid] and arr[mid]>=arr[mid+1]:
                return mid
            elif arr[mid]>=arr[mid-1] and arr[mid]<=arr[mid+1]: 
#                 [3,4,5,1]
                  # [3,3,3,3] so we maintain ==
                start=mid
            else:
                end=mid
            