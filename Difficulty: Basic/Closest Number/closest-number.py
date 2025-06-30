class Solution:
    def closestNumber(self, n, m):
        # code here 
        if n%m==0:
            return n
        
        small=(n//m)*m
        great=((n//m)+1)*m
        if abs(n-small)<abs(great-n):
            return small
        elif abs(n-small)>abs(great-n):
            return great
        else:
            return small if abs(small)>abs(great)else great
    
                
            