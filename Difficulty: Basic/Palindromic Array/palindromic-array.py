# Your task is to complete this function
# Function should return true/false
def isPalinArray(arr):
    # Code here
    c=0
    for i in arr:
        if str(i)==str(i)[::-1]:
            c+=1
    if c==len(arr):
        return True
    return False
#{ 
 # Driver Code Starts
# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().strip().split()))
        if isPalinArray(arr):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends