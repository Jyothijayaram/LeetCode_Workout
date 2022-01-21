class Solution:
    def duplicates(self, arr, n):
        hm = {}
        r = []
        for i in range(n):
            if arr[i] in hm:
                hm[arr[i]] += 1
            else:
                hm[arr[i]] = 1
        for k in hm:
            if hm[k] > 1:
                r.append(k)
        return sorted(r) if r else [-1]
    	    

#{ 
#  Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends