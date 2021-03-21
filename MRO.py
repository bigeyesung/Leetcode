class X():
    def who_am_i(self):
        print("I am a X")
    
class Y():
    def who_am_i(self):
        print("I am a Y")
    
class A(X, Y):
    pass
    
class B(Y, X):
    pass
        

# class C(X, Y):
#     def who_am_i(self):
#         print("I am a C")

class F(A, B):
    pass


obj=F()
obj.who_am_i()
print(F.mro())



# class A:
#     def process(self):
#         print('A process()')


# class B:
#     def process(self):
#         print('B process()')


# class C(B, A):
#     pass


# obj = C()  
# obj.process()    
# print(C.mro())   # print MRO for class C

#check tutorial
#http://www.srikanthtechnologies.com/blog/python/mro.aspx