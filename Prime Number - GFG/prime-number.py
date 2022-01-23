#User function Template for python3

class Solution:
    def isPrime (self, N):
        if N <=1:
            return 0
        else:
            c=2
            while(c*c<=N):
                if N % c==0:
                    return 0
                c+=1
            return 1
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.isPrime(N))
# } Driver Code Ends