#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s):
        dict={}
        curr_sum=0
        for i in range(len(arr)):
            curr_sum=curr_sum+arr[i]
            if curr_sum == s:
                return [1,i+1]
            if curr_sum - s in dict:
               return [dict[curr_sum-s]+2,i+1] 
            dict[curr_sum]=i
        return [-1]
        
        
       #Write your code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends