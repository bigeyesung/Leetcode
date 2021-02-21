#DFS
#up down,left,right dirs
arr = [
[float("inf"),  -1,  0 , float("inf")],
[float("inf"), float("inf"), float("inf"),-1],
[float("inf"),  -1, float("inf"),  -1],
[0, -1, float("inf"), float("inf")] 
]
        
class Solution():
    def search(self,arr):
        #time: O(row*col*N)
        #space:O(N)
        def dfs(row,col,arr,length):
            if not (0<=row<len(arr) and 0<=col<len(arr[0]) and arr[row][col]>=length):
                return 
            arr[row][col] = length
            dfs(row+1,col,arr,length+1)
            dfs(row-1,col,arr,length+1)
            dfs(row,col+1,arr,length+1)
            dfs(row,col-1,arr,length+1)
    #iterate the arr if it is "inf"
        for row in range(len(arr)):
            for col in range(len(arr[0])):
                if arr[row][col]==0:
                    dfs(row,col,arr,0)
        #time: O(row*col+N)
        #space:O(N)
    def bfs(self, arr):
        queue = []
        dirs = [[0,-1],[-1,0],[0,1],[1,0]]
        for row in range(len(arr)):
            for col in range(len(arr[0])):
                if arr[row][col]==0:
                    queue.append([row,col])
        while(queue):
            row = queue[0][0]
            col = queue[0][1]
            queue.pop(0)
            for d in dirs:
                new_row = row+d[0]
                new_col = col+d[1]
                if not (0<=new_row<len(arr) and 0<=new_col<len(arr[0]) and arr[new_row][new_col]>=arr[row][col]+1):
                    continue
                arr[new_row][new_col] = arr[row][col]+1
                queue.append([new_row,new_col])

if __name__ == "__main__":
    print(arr)
    sol = Solution()
    # sol.search(arr)
    sol.bfs(arr)
    print(arr)