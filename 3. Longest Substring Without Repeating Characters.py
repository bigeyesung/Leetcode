class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    #question: s = "abcabcbb" ->> 
    
    #data
    #input: lower case letters, no other chars, min len: 0
    #output: integer
    
    #test
    #corner case: "", "b", "bbb"
    #test case: "abcabcbb"
    
    #"abcabcbb"
    #"a"
    #"ab"
    #"abc"
    #"bca"
    #"cab"
    
    #iterate the string fron 0 to last index
    #   if substring[start:curIdx] has no repeating chars, continue
    #   else: remove substr[start] until substring does not have repeatring chars
    
        maxLen=0
        start=0
        end=0
        table={}
        while(end<len(s)):
            if table.get(s[end])==None:
                table[s[end]]=1
                maxLen=max(maxLen,end-start+1)
                end+=1
            else:
                while(table.get(s[end])!=None):
                    table[s[start]]-=1
                    if table[s[start]]==0:
                        del table[s[start]]
                    start+=1
        return maxLen

if __name__ == "__main__":
    sol=Solution()
    s = "abcabcbb"
    sol.lengthOfLongestSubstring(s)