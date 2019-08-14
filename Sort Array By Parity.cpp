class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& A) 
    {
    //vector B save even number
    //vector C save odd number
    
    vector<int>B;
    vector<int>C;
    for(int i=0;i<A.size();i++)
    {
        if(A[i]%2==0)
            B.push_back(A[i]);
        else
            C.push_back(A[i]);
    }
      
    //add vectorC to vectorB 
    for(int i=0;i<C.size();i++)
    {
        B.push_back(C[i]);
        
    }
        
        return B;
    }


}
