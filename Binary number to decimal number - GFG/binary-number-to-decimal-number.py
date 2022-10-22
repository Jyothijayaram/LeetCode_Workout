#User function Template for python3

class Solution:
	def binary_to_decimal(self, str):
	    temp=int(str)
	    base=1
	    deci=0
	    while temp:
	        last_digit=temp%10
	        temp=temp//10
	        deci=deci+last_digit*base
	        base=base*2
	    return deci
		# Code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		str = input()
		ob = Solution();
		ans = ob.binary_to_decimal(str)
		print(ans)
# } Driver Code Ends