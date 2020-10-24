# check if it is power2 or not
# new method testing performance
def Ispower2(num):
    ispower2=True
    count=0
    base=1
    while(base<=num):
        base = base*2
        count += 1
    if pow(2,count-1)!=num:
        ispower2=False
    return ispower2, count-1

def counterGame(tests):
    for test in tests:
        num = int(test)
        turn = 0
        while(num!=1):
            ispower2, count = Ispower2(num)
            if ispower2:
                num=num//2
            else:
                num = num - pow(2,count)
            turn += 1
        if turn%2!=0:
            print("louise\n")
        else:
            print("Ri\n")

if __name__ == "__main__":
    tests = ["6"]
    ret = counterGame(tests)