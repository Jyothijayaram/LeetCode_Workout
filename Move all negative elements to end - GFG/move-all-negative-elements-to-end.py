#User function Template for python3

class Solution:
    def segregateElements(self, arr, n):
        pos_lst=[]
        neg_lst=[]

        for i in arr:
            if i>0:
                pos_lst.append(i)
            else:
                neg_lst.append(i)
        arr.clear()
        for j in pos_lst:
            arr.append(j)
        for k in neg_lst:
            arr.append(k)
       
#{ 
#  Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        ob.segregateElements(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends