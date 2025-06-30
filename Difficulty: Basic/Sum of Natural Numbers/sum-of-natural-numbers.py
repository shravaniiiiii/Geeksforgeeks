class Solution:
    def findSum(self, n):
        # code here
        a=0
        i=1
        while i!=n+1:
            a+=i
            i+=1
        return a
