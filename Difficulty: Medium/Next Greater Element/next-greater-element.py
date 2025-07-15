class Solution:
    def nextLargerElement(self, arr):
        # code here
        stack=[]
        n=len(arr)
        res=[-1]*n
        for i in range(n - 1, -1, -1):
            while stack and stack[-1] <= arr[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1]
            stack.append(arr[i])
        return res