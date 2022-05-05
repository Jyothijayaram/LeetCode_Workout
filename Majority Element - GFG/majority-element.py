#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):
        if N==1:
            return A[0]
            
        dictt={}
        
        for i in A:
            if i in dictt:
                dictt[i]=dictt[i]+1
                
                if dictt[i] > N/2:
                    return i
            else:
                dictt[i]=1
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