#User function Template for python3
class Solution:
	def removeVowels(self, S):
	    result= [let for let in S if let not in ['a','e','i','o','u']]
	    S="".join(result)
	    return S
	    
	    
	    
	    
	    
		# code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		
		ob = Solution()	
		answer = ob.removeVowels(s)
		
		print(answer)


# } Driver Code Ends