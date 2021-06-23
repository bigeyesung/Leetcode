class Solution:
    def maximumSwap(self, num: int) -> int:
        # 2736->7236
        # 9973-> no
        #iterate every two digits,
        #find out the maximum number
        curMax = num
        num=[digit for digit in str(num)]
        ans = num[:]
        ori = num.copy()

        for ind in range(len(num)):
            for ind1 in range(ind,len(num)):
                if num[ind1]>num[ind]:
                    num[ind],num[ind1]=num[ind1],num[ind]
                    if int("".join(num))>curMax:
                        # if("".join(num))==9931:
                        #     print("pause")
                        curMax=int("".join(num))
                    #update num
                    num = ori.copy()
        return curMax

    def maximumSwap1(self, num):
        A = list(str(num))
        ans = A[:]
        B=A
        print(id(A))
        print(id(ans))
        print(id(B))
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                A[i], A[j] = A[j], A[i]
                if A > ans: ans = A[:]
                A[i], A[j] = A[j], A[i]

        return int("".join(ans))

    def maximumSwap2(self, num):
        A = map(int, str(num))
        last = {x: i for i, x in enumerate(A)}
        for i, x in enumerate(A):
            for d in range(9, x, -1):
                if last.get(d, None) > i:
                    A[i], A[last[d]] = A[last[d]], A[i]
                    return int("".join(map(str, A)))
        return num

sol=Solution()
sol.maximumSwap2(1993)