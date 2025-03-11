#User function Template for python3

class Solution:
    def firstRepeated(self, arr):
        seen = {}  # Store first occurrence index
        min_index = float('inf')

        for i, num in enumerate(arr):
            if num in seen:
                min_index = min(min_index, seen[num])  # Update with smallest index
            else:
                seen[num] = i + 1  # Store 1-based index

        return min_index if min_index != float('inf') else -1
       

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstRepeated(arr))
        print("~")

# } Driver Code Ends