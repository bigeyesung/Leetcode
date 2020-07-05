# Python code to demonstrate the working of 
# bisect(), bisect_left() and bisect_right() 
  
# importing "bisect" for bisection operations 
import bisect 
  
# initializing list 
li = [1, 3, 4, 4, 4, 6, 7] 

# initializing list 
li1 = [1, 3, 4, 4, 4, 6, 7] 

bisect.insort(li1, 5) 

# using bisect() to find index to insert new element 
# returns 5 ( right most possible index ) 
print ("The rightmost index to insert, so list remains sorted is  : ", end="") 
print (bisect.bisect(li, 6)) 

# using bisect_left() to find index to insert new element 
# returns 2 ( left most possible index ) 
print ("The leftmost index to insert, so list remains sorted is  : ", end="") 
print (bisect.bisect_left(li, 3)) 
  
# using bisect_right() to find index to insert new element 
# returns 4 ( right most possible index ) 
print ("The rightmost index to insert, so list remains sorted is  : ", end="") 
print (bisect.bisect_right(li, 4, 0, 4)) 