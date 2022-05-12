#User function Template for python3
class Solution:
	def pattern(self, S):
	     n=len(S)
         l=[]
         for i in range(n):
             l.append(S[:n-i])
         return l
    	        
	        
		# code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.pattern(S)
		for value in answer:
			print(value)
			

# } Driver Code Ends