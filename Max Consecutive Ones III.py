'''
Intuition
Translation:
Find the longest subarray with at most K zeros.


Explanation
For each A[j], try to find the longest subarray.
If A[i] ~ A[j] has zeros <= K, we continue to increment j.
If A[i] ~ A[j] has zeros > K, we increment i.
'''
s = "abc"
t = "abcd"
arr = [i for i in t if i not in s]
arr2 = [i for i in s if i  in t]

def longestOnes(A, K):
    i = 0
    for j in range(len(A)):
        K -= 1 - A[j]
        if K < 0:
            K += 1 - A[i]
            i += 1
    return j - i + 1

A = [1,1,1,0,0,0,1,1,1,1,0]
K = 2

ans = longestOnes(A,K)
print(ans)