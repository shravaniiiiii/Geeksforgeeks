class Solution:
    def sumOfDigits(self, n):
        # code here
        s=0
        while n>0:
            r=n%10
            s+=r
            n//=10
        return s
        