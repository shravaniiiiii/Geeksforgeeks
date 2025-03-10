class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self, arr, x):
        #Your code here
        c=-1
        for i in range(len(arr)-1,-1,-1):
            if arr[i]<=x:
                return i
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        x = int(input().strip())
        ob = Solution()
        ans = ob.findFloor(arr, x)
        print(ans)
        tc -= 1

# } Driver Code Ends