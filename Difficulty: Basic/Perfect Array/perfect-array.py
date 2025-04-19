class Solution:
    def isPerfect(self, arr):
        # code here
        n= len(arr)
        if n== 0:
            return true;
            
        i= 1
        while i < n and arr[i] > arr[i-1]:
            i+=1;
            
        while i <n and arr[i] == arr[i-1]:
            i += 1;
            
        while i < n and arr[i] < arr[i-1]:
            i+= 1;
            
        return i == n    
            
            
                
                


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        solution = Solution()
        print("true" if solution.isPerfect(arr) else "false")
        print("~")

# } Driver Code Ends