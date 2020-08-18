def maxVacationDays(flights, days):
    n = len(flights)
    k = len(days[0])
    dp = [0]*n
    for j in range(k):
        t = [0]*n
        for i in range(n):
            for p in range(n):
                if (i==p or flights[p][i]):
                    t[i] = max(t[i], dp[p] + days[i][j])
        dp = t
    return max(dp)


def maxVacationDays2(flights, days):
    """
    :type flights: List[List[int]]
    :type days: List[List[int]]
    :rtype: int
    """
    N, K = len(days), len(days[0])
    dp = [0] + [-1] * (N - 1)
    for w in range(K):
        ndp = [x for x in dp]
        for sc in range(N):
            if dp[sc] < 0: continue
            for tc in range(N):
                if sc == tc or flights[sc][tc]:
                    ndp[tc] = max(ndp[tc], dp[sc] + days[tc][w])
        dp = ndp
    return max(dp)

flights = [[0,0,0],[0,0,0],[0,0,0]]
days = [[1,1,1],[7,7,7],[7,7,7]]

ret = maxVacationDays2(flights, days)
print(ret)