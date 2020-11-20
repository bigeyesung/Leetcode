# Necesssary condition: All nodes with no in-degree must in the final result,
# because they can not be reached from
# All other nodes can be reached from any other nodes.
# Sufficient condition: All other nodes can be reached from some other nodes.
class Solution:
    def findSmallestSetOfVertices(self, n, edges):
        tmp1 = set(range(n))
        tmp2 = set(j for i, j in edges)
        tmp3 = tmp1-tmp2
        return list(set(range(n)) - set(j for i, j in edges))

if __name__ == "__main__":
    sol = Solution()
    num = 6
    arr = [[0,1],[0,2],[2,5],[3,4],[4,2]]
    ret = sol.findSmallestSetOfVertices(num, arr)
    print(ret)