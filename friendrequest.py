import collections
def numFriendRequests(ages):
    def request(a, b):
        return not (b <= 0.5 * a + 7 or b > a or b > 100 and a < 100)
    c = collections.Counter(ages)
    tmp = c[16]s
    for a in c:
        for b in c:
            tmp1 = request(a, b)
            tmp2 = c[a]
            tmp3 = (c[b] - (a == b))
            tmp = request(a, b) * c[a] * (c[b] - (a == b))
            print(tmp)

    # return sum(request(a, b) * c[a] * (c[b] - (a == b)) for a in c for b in c)

ages = [16,16]


ret = numFriendRequests(ages)