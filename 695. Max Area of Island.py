class Solution:
    def __init__(self):
        self.curLand=0

    def maxAreaOfIsland(self, grid) -> int:
        #question:
        #land-> max area of land
        
        #data:
        #input:2d array, only 1 and 0, min len is 1
        #output: intger
        
        #tests/corner cases:
        #corner cases: [0], [1], 
        #test: [0 1 0]
        #  ^
        #<-1->
        #  ^
        
        #iterate the 2d array row by row:
        #   for each iteration: 
        #       if we find it is "1", and not seem before,
        #       we start dfs search in 4 directions
        #       search end when no new "1" is found, count the founded land 
        #       compare founded land with maxFound
        def DfsSearch(row,col):
            for dir in dirs:
                newRow=row+dir[0]
                newCol=col+dir[1]
                if 0<=newRow<rows and 0<=newCol<cols and grid[newRow][newCol]==1:
                    grid[newRow][newCol]="#"
                    self.curLand+=1
                    DfsSearch(newRow,newCol)  

        
        #create seen table
        # seen=[]
        dirs=[[0,1],[0,-1],[1,0],[-1,0]]
        rows = len(grid)
        cols = len(grid[0])
        maxLand=0
        
        # for row in range(rows):
        #     tmp=[False]*cols
        #     seen.append(tmp)
        #T:O(n*h), h=tree height
        #S:O(1)
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1:
                    grid[row][col]="#"
                    self.curLand+=1             
                    DfsSearch(row,col)
                #compare current countLand with maxLand:
                maxLand=max(self.curLand,maxLand)
                self.curLand=0
        return maxLand

if __name__ == "__main__":
    sol=Solution()
    grid=[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
    ret=sol.maxAreaOfIsland(grid)
    print(ret)