grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]

def CountNeg(grid):
    #ietrate each row
    #for each row: binary search to find 1st neg index
    count = 0
    for row in grid:
        n = len(row)
        l,r = 0,n-1
        while(l<=r):
            mid = (l+r)//2
            if row[mid]>=0:
                l=mid+1
            else:
                r=mid-1
        count+=n-l
    return count


if __name__ == "__main__":
    ret = CountNeg(grid)