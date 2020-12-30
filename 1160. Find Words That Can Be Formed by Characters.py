#time: O(N_chars+N_words)
#O(N_chars):create a counter for chars
#O(N_words):create wordcounter times words#
#Space:O(N_chars+N_word)
import collections
class Solution:
    def countCharacters(self, words, chars):
        #create return varable
        totalcount = 0
        #create a counter for chars:
        counter = collections.Counter(chars)
        #iterate the words:
        for word in words:
        #  for each word create another wordcounter
        #compare wordcounter and counter: char, times.
            wordcounter = collections.Counter(word)
            countword = True
            for key in wordcounter:
                if not (counter.get(key)!=None and wordcounter[key]<=counter[key]):
                    countword = False
                    break
            if countword:
                totalcount+=len(word)          
        return totalcount
        #corner cases:
        #words = ["a"], chars = "b"
        #if not found->return 0
        
    def countCharacters1(self, words, chars):
        count = 0
        for word in words:
            temp = chars
            for i, char in enumerate(word):
                if char not in temp:
                    break
                temp = temp.replace(char, "", 1)
                # if we get here we can make a word from chars
                if i == len(word) - 1:
                    count += len(word)
        return count            

    def test(self,words,chars):
        count=0
        for word in words:
            temp = chars
            n = len(word)
            for ind in range(n):
                if word[ind] not in temp:
                    break
                temp=temp.replace(word[ind],"",1)
                if ind == n-1:
                    count+=n
        return count
if __name__ == "__main__":
    
        