#User function Template for python3

class Solution:        
    def primeRange(self,M,N):
            is_prime=[True for t in range(N+1)]
            p=2
            while(p*p<=N):
                if is_prime[p]:
                    for m in range(p**2,N+1,p):
                        is_prime[m]=False
                p+=1
            is_prime[0]=False
            is_prime[1]=False
            return [p for p in range(M,N+1) if is_prime[p]]
            
            
        
            
            
            
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        M,N=map(int,input().strip().split(" "))
        ob=Solution()
        ans=ob.primeRange(M,N)
        for i in ans:
            print(i,end=" ")
        print()    
# } Driver Code Ends