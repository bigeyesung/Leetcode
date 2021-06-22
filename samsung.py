class MovingTotal:
    def __init__(self):
        self.container=[]
        self.total=0
        self.index=0
        self.table = {}

    def append(self, numbers):
        """
        :param numbers: (list) The list of numbers.
        """
        increase=len(numbers)
        self.container.extend(numbers)
        #check 3 numbers
        #if len>=3
        if len(self.container)==3:
            num = sum(self.container)
            self.total=num
            self.table[num]=num
            self.index+=3
        elif len(self.container)>3:
            for ind in range(self.index, len(self.container)):
                self.total = self.total-self.container[ind-3]+self.container[ind]
                print(self.total)
                self.table[self.total]=self.total
            self.index+=increase
        



    def contains(self, total):
        """
        :param total: (int) The total to check for.
        :returns: (bool) If MovingTotal contains the total.
        """
        if self.table.get(total)!=None:
            return True
        else:
            return False
    
if __name__ == "__main__":
    movingtotal = MovingTotal()
    movingtotal.append([1])
    print(movingtotal.contains(1))
    movingtotal.append([2])
    print(movingtotal.contains(2))
    movingtotal.append([3])
    movingtotal.append([4,5,6,7])
    print(movingtotal.contains(18))