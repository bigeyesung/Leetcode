from collections import defaultdict,Counter
import heapq

class Solution:
    def mostCommonWord(self, paragraph, banned):
        # first we need to remove the symbols that can be present, and replacing with space
        symbols = "!?',;."
        for i in symbols:
            paragraph = paragraph.replace(i, " ")
        hashMap = defaultdict(int)
        # converting to lower case
        paragraph = paragraph.lower()
        # splitting based on space to put the given words to a list
        list1 = paragraph.split() #default separator is any whitespace.

        # checking if the word not in banned , and incrementing its count
        for i in list1:
            if i not in banned:
                hashMap[i] = hashMap[i] + 1

        # finding the word has occurs most number of times, O(n**2)
        maximum = max(hashMap.values())

        # finding the value of key for the word with maximum count
        for key, value in hashMap.items():
            if value == maximum:
                return key
    def mostCommonWord1(self, paragraph, banned):
        # first we need to remove the symbols that can be present, and replacing with space
        symbols = "!?',;."
        for i in symbols:
            paragraph = paragraph.replace(i, " ")
        hashMap = defaultdict(list)
        # converting to lower case
        paragraph = paragraph.lower()
        # splitting based on space to put the given words to a list
        list1 = paragraph.split()
        heap=[]
        heapq.heapify(heap)
        counter=Counter(list1)
        for word in counter:
            if word not in banned:
                hashMap[counter[word]].append(word)
                heapq.heappush(heap,counter[word])
                if len(heap)>1:
                    heapq.heappop(heap)
        # finding the word has occurs most number of times
        maximum=heapq.heappop(heap)
        words=hashMap[maximum][0]
        return words


if __name__=="__main__":
    nums=[]
    sol=Solution()
    para="Bob hit a ball, the hit BALL flew far after it was hit."
    banned=["hit"]
    ret=sol.mostCommonWord(para,banned)
    print(ret)        