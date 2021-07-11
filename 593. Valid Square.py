class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        #find all posible lengths 
        #sort the length
        #the lenght must be 1:1:sqrt(2)
        def Sqe(p,q):
            return (p[0]-q[0])**2+(p[1]-q[1])**2
        arr=[Sqe(p1,p2),Sqe(p1,p3),Sqe(p1,p4),Sqe(p2,p3),Sqe(p2,p4),Sqe(p3,p4)]
        arr.sort()
        
        if 0<arr[0]==arr[1]==arr[2]==arr[3] and arr[4]==arr[5]==arr[3]*2:
            return True
        else:
            return False