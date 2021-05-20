import collections
import enum as Enum:
class Way:
    IN=0
    EXIT=1
    NOCHANGE=2
def turnstile(time, direction):
    #create a time counter loop, stop when all people are set
    timeCounter=0
    countPpl=0
    timeTable=collections.defaultdict(list)
    conflict=[]
    preTime=[]
    retArr=[-1]*len(time)
    for ind in range(len(time)):
        timeTable[time[ind]].append(ind)
    while(countPpl!=len(time)):
        if timeTable.get(timeCounter)!=None:
            slot= timeTable[timeCounter]
            if len(slot)==1 and not conflict:
                retArr[slot[0]]=1
                countPpl+=1
            elif len(slot)==1 and conflict:
                #if they are in the same sec
                if time[slot[0]]==time[conflict[0]]:
                    conflict.append(slot[0])
                    continue
            elif len(slot)==2:
                ppl1=slot[0]
                ppl2=slot[1]
                dir1=direction[ppl1]
                dir2=direction[ppl2]
                if not preTime or preTime[-1]==Way.EXIT.value or preTime[-1]==Way.NOCHANGE.value:
                    if dir2==Way.EXIT.value:
                        retArr[ppl2]=1
                        conflict.append(ppl1)
                    else:
                        retArr[ppl1]=1
                        conflict.append(ppl2)
                    countPpl+=1
                    preTime.append(Way.EXIT.value)
                elif preTime[-1]==Way.IN.value:
                    if dir2==Way.IN.value:
                        retArr[ppl2]=1
                        conflict.append(ppl1)
                    else:
                        retArr[ppl1]=1
                        conflict.append(ppl2)
                    countPpl+=1
                    preTime.append(Way.IN.value)
    
        else:
            preTime.append(Way.NOCHANGE.value)


        #if ith sec has people:
        #   if no conflit-> update the retArr
        #   ele if conflict:
        #       if pre sec stile not used:
        #       elif pre sec stile is exit state
        #       elif pre sec stile is enter state

        #add one sec
        timeCounter+=1