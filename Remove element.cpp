    int removeElement(vector<int>& nums, int val) 
    {
    //basically move non-val to the left-handed side
    //index: val index    
    int index=0;
    for(int i=0;i<nums.size();i++)
     {
         
        if(nums[i]!=val)
         {
             std::swap(nums[i],nums[index]);
             index++;
         }

     }
     return index;   
        
    }