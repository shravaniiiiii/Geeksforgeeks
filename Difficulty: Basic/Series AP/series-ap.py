
class Solution:
    def nthTermOfAP(self, a1 : int, a2 : int, n : int) -> int:
        # code here
        c=0
        a=[]
        d=a2-a1
        i=a1
        while c!=n:
            a.append(i)
            i+=d
            c+=1
        return a[n-1]
            
        
