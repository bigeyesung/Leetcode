def longestOnes(A, K):
    i = 0
    for j in range(len(A)):
        # K -= 1 - A[j]
        K = K - 1 + A[j]
        if K < 0:
            K += 1 - A[i]
            i += 1
    return j - i + 1

a = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
ans = longestOnes(a,k)