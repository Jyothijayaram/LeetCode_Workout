#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):
        m = {}
        for i in range(N):
            
            if A[i] in m:
                m[A[i]] += 1
            else:
                m[A[i]] = 1
        count = 0
        for key in m:
            if m[key] > N / 2:
                count = 1
                return key
        if(count == 0):
            return -1
        
        #Your code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends