
def invalidTransactions(transactions):    
    ans = set()
    for idx in range(len(transactions)):
        cur = transactions[idx].split(',')
        
        #check amount
        if int(cur[2]) > 1000:
            ans.add(','.join(cur))
            
        #check 60mins in different city
        for idx1 in range(idx + 1, len(transactions)):
            next = transactions[idx1].split(',')
            if cur[0] == next[0] and cur[3] != next[3] and abs(int(cur[1]) - int(next[1])) <= 60:
                ans.add(','.join(cur))
                ans.add(','.join(next))
    return list(ans)


test = ["alice,20,800,mtv","alice,50,100,beijing"]
invalidTransactions(test)