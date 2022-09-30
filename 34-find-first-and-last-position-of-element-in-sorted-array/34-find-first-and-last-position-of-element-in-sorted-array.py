class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.bin_search(nums,target,True)
        right = self.bin_search(nums,target,False)
        return [left,right]
        
    def bin_search(self,nums,target,leftmost):

        i=-1
        start,end=0,len(nums)-1

        while(start<=end):
            mid=(start+end)//2

            if target > nums[mid]:
                start=mid+1

            elif target < nums[mid]:
                end=mid-1

            else:
                i=mid
                if leftmost:
                    end=mid-1
                else:
                    start=mid+1
        return i



        return [-1,-1]