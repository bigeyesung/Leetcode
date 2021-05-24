#question:
averageUtil = [25, 23, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 76, 80]
#Average utilization < 25%: reduce the number of instances by half(if instances >1)
#25% <= Average utilization <= 60%: nothing 
#Average utilization > 60%: double the number of instances if the doubled value does not exceed 2* 10^8.
#                           if bigger that threshold, do nothing
#if action happends(double or decrease): index+11


def finalInstances(instances, averageUtil):
    import math
    index=0
    threshold=2* 10**8
    while(index<len(averageUtil)):
        takeAction=False

        if averageUtil[index]<25:
            if instances>1:
                instances=math.ceil(instances/2)
                takeAction=True

        elif averageUtil[index]>60:
            newInstances=instances*2
            if newInstances<=threshold:
                instances=newInstances
                takeAction=True

        index+=1
        if takeAction:
            index+=10
    return instances


instances=100000000
averageUtil = [30,95,4,8,19,89]
ret=finalInstances(instances, averageUtil)
