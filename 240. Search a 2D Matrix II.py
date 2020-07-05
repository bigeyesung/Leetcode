def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    # check rowX[0]<=target:
    # for each row: go binary search
    for row in range(len(matrix)):
        if matrix[row][0] == target:
            return True
        elif matrix[row][0] < target:
            left = 0
            right = len(matrix[row])-1
            while(left<=right):
                middle = int((left+right)/2)
                if target==matrix[row][middle]:
                    return True
                elif target<matrix[row][middle]:
                    right = middle-1
                else:
                    left = middle+1
    return False