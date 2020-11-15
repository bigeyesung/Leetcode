# Time:  O(n)
# Space: O(1)
from collections import Counter
from collections import defaultdict
class Solution():
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        dic = defaultdict(list)
        counter = Counter()
        left, max_length = 0, 0
        for right, char in enumerate(s):
            counter[char] += 1
            while len(counter) > k:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            print("current sub: ", s[left:right+1])
            # all posible strings
            dic[right-left+1].append(s[left:right+1])
            max_length = max(max_length, right-left+1)
        
        return max_length

    def test(self, s, k):
        # for-loop to iterate
        #   right ptr to add char
        #   left prt to remove char
        #   while sub str char type > k: remove left char,
        dic, counter = defaultdict(list), Counter()
        left, max_lenth = 0,0
        for right, char in enumerate(s):
            counter[char]+=1
            while(len(counter)>k):
                #do sth
                counter[s[left]]-= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            print("cur sub: ", s[left:right+1])
            dic[right-left+1].append(s[left:right+1])
            max_lenth = max(max_lenth, right-left+1)
        return max_lenth


if __name__ == "__main__":
    sol = Solution()
    string = "abcbbbbcccbdddadacb" 
    ret = sol.test(string,2)
    print(ret)