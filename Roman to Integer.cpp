
    int romanToInt(string s) 
    {
        if (s.empty()) return 0;
        int sum=0;
        
        //save in hashmap
        unordered_map<char,int>table = 
        {
            {'I',1},
            {'V',5},
            {'X',10},
            {'L',50},
            {'C',100},
            {'D',500},
            {'M',1000}
            
        };
        //iterate for each ch
        for(int i=0;i<s.length()-1;i++)
        {
            if(table[s[i]]<table[s[i+1]])
            {
                sum-=table[s[i]];
            }
            else
            {
                sum+=table[s[i]];
            }
        }
        //check boder
        sum+=table[s.back()];
        return sum;
    }