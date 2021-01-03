import collections
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        #create a dic
        #town judge: it has N-1 connections
        #iterate dic see if one satisfy requirement
        #corner case: trust length == 0/only judge exist
        if N ==1:
            return 1
        
        dic = collections.defaultdict(list)
        candidate = None
        for item in trust:
            dic[item[1]].append(item[0])
        for judge in dic:
            if len(dic[judge])==N-1:
                candidate = judge
                break
        
        for judge in dic:
            if candidate in dic[judge]:
                candidate = None
        if candidate:
            return candidate
        else:
            return -1