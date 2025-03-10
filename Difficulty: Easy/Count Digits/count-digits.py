#User function Template for python3

class Solution:
    def evenlyDivides(self, n):
        # code here
        c=0
        a=str(n)
        for i in a:
            if int(i)!=0 and n%int(i)==0:
                c+=1
        return c
        
            
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.evenlyDivides(N))
        print("~")

# } Driver Code Ends