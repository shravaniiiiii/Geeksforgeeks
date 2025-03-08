#User function Template for python3

class Solution:
    def maxProduct(self, arr):
        # code here
        max1 = max2 = max3 = float('-inf')
        min1 = min2 = float('inf') 
        for i in arr:
            if i>max1:
                max3,max2,max1=max2,max1,i
            elif i>max2:
                max3,max2=max2,i
            elif i>max3:
                max3=i
            if i<min1:
                min2,min1=min1,i
            elif i<min2:
                min2=i
        return max(max1*max2*max3,min1*min2*max1)
        
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1
        print("~")
# } Driver Code Ends