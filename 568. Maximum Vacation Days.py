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


flights = [[0,0,0],[0,0,0],[0,0,0]]
days = [[1,1,1],[7,7,7],[7,7,7]]

ret = maxVacationDays(flights, days)
print(ret)