 int arrayPairSum(vector<int>& nums) 
    {
        //sort nums first
        sort(nums.begin(),nums.end());
        //get pair can get min sum
        int sum=0;
        for(int i=0;i<nums.size()/2;i++)
        {
            sum = sum+nums[2*i];
        }
        
        return sum;
        
        //  vector<int> hashtable(20001,0);
        // for(size_t i=0;i<nums.size();i++)
        // {
        //     hashtable[nums[i]+10000]++;
        // }
        // int ret=0;
        // int flag=0;
        // for(size_t i=0;i<20001;){
        //     if((hashtable[i]>0)&&(flag==0)){
        //         ret=ret+i-10000;
        //         flag=1;
        //         hashtable[i]--;
        //     }else if((hashtable[i]>0)&&(flag==1)){
        //         hashtable[i]--;
        //         flag=0;
        //     }else i++;
        // }
        // return ret;
        
    }
