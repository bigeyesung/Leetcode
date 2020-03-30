class MovingTotal:
    def __init__(self):
        self._arr = []
        self._total = {}
    def append(self, numbers):
        """
        :param numbers: (list) The list of numbers.
        """
        if len(self._arr) == 3:
            # if full-> remove first one
            self.__arr.pop(0)

        else:
            
            self._arr.extend(numbers)
        
        pass

    def contains(self, total):
        """
        :param total: (int) The total to check for.
        :returns: (bool) If MovingTotal contains the total.
        """
        if self._total.get(total)!= None:
            return True
        else:
            return False
    
if __name__ == "__main__":
    movingtotal = MovingTotal()
    movingtotal.append([1, 2, 3])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    movingtotal.append([4])
    print(movingtotal.contains(9))