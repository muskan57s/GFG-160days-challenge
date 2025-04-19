#User function Template for python3

class Solution:
    def removeDuplicate(self, arr):
        # code here
        
        if not arr:
            return []
        
        result = []
        seen = set()
        
        i=0
        n = len(arr)
        
        while i < n:
            if arr[i] not in seen:
                
                result.append(arr[i])
                seen.add(arr[i])
            i += 1
            
        return result    




#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.removeDuplicate(arr)
        print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends