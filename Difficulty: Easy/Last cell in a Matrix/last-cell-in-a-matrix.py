#User function Template for python3

class Solution:
    def endPoints(self, matrix, R, C):
        i=0
        j=0
        dir=0
        while (i>=0 and i<R and j>=0 and j<C):
            if (matrix[i][j]==1):
                matrix[i][j]=0
                dir=(dir+1)%4
            if (dir==0):
                j+=1
            elif (dir==1):
                i+=1
            elif (dir ==2):
                j-=1
            else:
                i-=1
        if (dir==0):
            j-=1
        elif (dir==1):
            i-=1
        elif (dir==2):
            j+=1
        else:
            i+=1
        return(i,j)
            
        #code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        matrix = []
        for i in range(r):
            line = [int(x) for x in input().strip().split()]
            matrix.append(line)
        ob = Solution()
        ans = ob.endPoints(matrix,r,c)
        print('(',ans[0],', ',ans[1],')',sep ='')

        print("~")
# } Driver Code Ends