def longestArithSeqLength(A):
    dp = {}
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            key = (i, A[j] - A[i])
            tmp2 = dp.get(key, 1)
            dp[j, A[j] - A[i]] = tmp2 + 1
    return max(dp.values())

    # dp = {}
    # for i in range(len(A)):
    #     for j in range(i + 1, len(A)):
    #         dp[j, A[j] - A[i]] = dp.get((i, A[j] - A[i]), 1) + 1
    # return max(dp.values())


arr= [3,6,9,12]
asn = longestArithSeqLength(arr)
print(asn)