
#User function Template for python3

class Solution:
    
    #Function to find the maximum occurring character in a string.
    def getMaxOccurringChar(self,s):
        new_s=sorted(s)
        maxi=1
        a=sorted(list(set(new_s)))
     
        ans=new_s[0]
        for i in range(len(a)):
            if s.count(a[i])>maxi:
                maxi=s.count(a[i])
                ans=a[i]
        return ans 
            
                
        #code here
    
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        print(Solution().getMaxOccurringChar(s))
# } Driver Code Ends