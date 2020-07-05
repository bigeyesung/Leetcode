import collections
def customSortString(S, T):
    c, s = collections.Counter(T), set(S)
    tmp = ''.join(i * c[i] for i in S)
    for i in S:
        t = i * c[i]
        print(t)
    tmp2 = ''.join(i * c[i] for i in c if i not in s)
    return ''.join(i * c[i] for i in S) + ''.join(i * c[i] for i in c if i not in s)

S = "cba"
T = "abcdc"
customSortString(S,T)