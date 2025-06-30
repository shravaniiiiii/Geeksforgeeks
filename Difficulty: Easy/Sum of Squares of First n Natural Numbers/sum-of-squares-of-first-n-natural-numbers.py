#User function Template for python3
class Solution:
    # Function to calculate the sum of squares of first 'number' natural numbers
    def sumOfSquares(self, number):
        a=0
        i=1
        while i!=number+1:
            a+=i*i
            i+=1
        return a
        # code here