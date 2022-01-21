def transitionPoint(arr, n):
    res=0
    for i in range(n):
        res^=arr[i]
        if res!=0:
            return i
    return -1
            
    
    
    #Code here

#{ 
#  Driver Code Starts
#driver code
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(transitionPoint(arr, n))

# } Driver Code Ends