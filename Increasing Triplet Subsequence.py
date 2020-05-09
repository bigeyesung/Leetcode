import bisect
def increasingTriplet(nums):
    try:
        inc = [float('inf')] * 2
        for x in nums:
            inc[bisect.bisect_left(inc, x)] = x
        return False
    except:
        return True  


def increasingTriplet2(nums):
    inc = [float('inf')] * 2
    for x in nums:
        i = bisect.bisect_left(inc, x)
        if i >= 2:
            return True
        inc[i] = x
    return False

arr = [5,4,3,2,1]
ret = increasingTriplet(arr)
print(arr)