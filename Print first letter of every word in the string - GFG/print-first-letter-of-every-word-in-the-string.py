#User function Template for python3
class Solution:
	def firstAlphabet(self, S):
		# code here
			return "".join(list(map(lambda a: a[0], S.split())))
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.firstAlphabet(S)
		
		print(answer)


# } Driver Code Ends