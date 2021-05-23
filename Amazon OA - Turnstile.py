from enum import Enum

class Info(Enum):
    ARRTIME=0
    PERSON=1

class Pre(Enum):
    NOBODY=-1
    ENTER=0
    EXIT=1

def getTimes(numCustomers, arrTime, direction):
    en, ex = [], []
    res = [0] * len(arrTime)
    for i, t in enumerate(arrTime):
        if direction[i] == 1:
            #arrTime, Ith person
            ex.append([arrTime[i], i])
        else:
            en.append([arrTime[i], i])
    
    timeCounter, lastTurn = 0, Pre.NOBODY.value # time is 0 at the beginning and -1 
                                # indicates nothing happened at prior time
    while ex or en:
        # Process the exit queue if and only if following conditions are satisfied
        # If exit queue is not empty and the person at the front of the queue can go out based on his time stamp
        # and ( Nothing happened at last time stamp i.e. nobody moved in or out so lastTurn will be -1 in this case
        # or, somebody moved out at last time stamp, in this case lastTurn will be 1
        # or, nobody is there in the entrance queue
        # or, at last time stamp somebody got in but the person at the front of the queue can't go in due to their timestamp  
        if ex and ex[0][Info.ARRTIME.value] == timeCounter and \
        (lastTurn == Pre.NOBODY.value or lastTurn == Pre.EXIT.value or not en or (lastTurn == Pre.ENTER.value and en[0][Info.ARRTIME.value] > timeCounter)):
            res[ex[0][Info.PERSON.value]] = timeCounter
            lastTurn = Pre.EXIT.value
            ex.pop(0)
        elif en and en[0][Info.ARRTIME.value] == timeCounter:
            res[en[0][Info.PERSON.value]] = timeCounter
            lastTurn = Pre.ENTER.value
            en.pop(0)
        else:
            lastTurn = Pre.NOBODY.value

        timeCounter += 1
    
    return res

if __name__ == "__main__":
    # arrTime = [1, 1, 2, 6]
    # direction = [0, 1, 1, 0]
    arrTime = [1,2,4]
    direction = [0, 1, 1]
    ret=getTimes(len(arrTime), arrTime, direction)