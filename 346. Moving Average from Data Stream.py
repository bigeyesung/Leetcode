class MovingAverage():
    def __init__(self, size):
        self.__size = size
        self.__queue = []
    def next(self, num):
        #full size:pop first
        if len(self.__queue) == self.__size:
            self.__queue.pop(0)
        self.__queue.append(num)
        print("ans: ", sum(self.__queue)/len(self.__queue))
        return sum(self.__queue)/len(self.__queue)

if __name__ == "__main__":
    sol = MovingAverage(3)
    ret = sol.next(1)
    ret = sol.next(10)
    ret = sol.next(3)
    ret = sol.next(5)