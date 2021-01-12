class Solution:
    #find out odd num in even index
    #swap with even num in odd index
    #the idea is one odd num is in even index which means there must be one even num in odd index
    #T:O(n/2*n/2)
    #S:O(1)
    def sortArrayByParityII(self,A):
        odd_index=1
        for even_index in range(0,len(A),2):
            if A[even_index]%2!=0:#find odd num in even index
                while(A[odd_index]%2!=0):#find even num in odd index
                    odd_index+=2
                A[even_index],A[odd_index] = A[odd_index], A[even_index]
        return A
    def test1(self,A):
        odd_ind = 1
        for even_ind in range(0,len(A),2):
            if A[even_ind]!=0:
                while(A[odd_ind]%2!=0):
                    odd_ind+=2
                A[even_ind],A[odd_ind] = A[odd_ind], A[even_ind]
        return A
if __name__ == "__main__":
    arr = []
    ret = "".join(arr)
    sol = Solution()
    arr= [4,1,0,2,7,3]
    ret = sol.test(arr)
    print(arr)
    print(ret)