class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) 
    {
     unordered_map<int,int>table;
     unordered_map<int,int>::iterator it;
     vector<int>vec;
     for(int i=0;i<nums.size();i++)
     {
         it = table.find(target-nums[i]);
         if(it!=table.end())
         {
             vec.push_back(i);
             vec.push_back(it->second);
             break;
         }
         else
         {
             table.insert(pair<int,int>(nums[i],i));
         }
             
     }
        
        return vec;