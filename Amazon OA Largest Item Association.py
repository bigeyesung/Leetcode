import collections
#input: [[Item1, Item2], [Item3, Item4], [Item4, Item5]]
#output: [Item3, Item4, Item5]


#create a connection table
#find out all unique element
#iterate all unique element and save and connected path

class Solution():
    def findAsso(self,relationships):
        connect=collections.defaultdict(list)
        uniqueSet=set()
        retSet=set()
        maxLen=0
        for pair in relationships:
            connect[pair[0]].append(pair[1])
            connect[pair[1]].append(pair[0])
            uniqueSet.add(pair[0])
            uniqueSet.add(pair[1])
        
        for item in uniqueSet:
            queue=[item]
            seen={item:item}
            curArr=[]
            while(queue):
                levelCount=len(queue)
                while(levelCount!=0):
                    #add the ele to the group
                    node= queue.pop(0)
                    curArr.append(node)
                    nextLevel=connect[node]
                    for item in nextLevel:
                        if seen.get(item)==None:
                            queue.append(item)
                            seen[item]=item
                    levelCount-=1
            if len(curArr)>=maxLen:
                maxLen=len(curArr)
                retSet.add(tuple(curArr))
        return list(retSet)

if __name__ == "__main__":
    sol=Solution()
    relations=[["Item1", "Item2"], ["Item3", "Item4"], ["Item4", "Item5"]]
    ret=sol.findAsso(relations)
    print(ret)
                


