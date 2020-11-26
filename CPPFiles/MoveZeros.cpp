class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int lastNonZeroIDX = 0;
        int numZeros = 0;
        for(unsigned int i = 0; i < nums.size(); ++i)
        {
            if(nums[i] != 0)
            {   
                nums[lastNonZeroIDX] = nums[i];
                lastNonZeroIDX = lastNonZeroIDX + 1;
            }
            else
            {
                numZeros = numZeros + 1;
            }
        }
        for(unsigned int i = lastNonZeroIDX; i < nums.size(); ++i)
        {
            nums[i] = 0;
        }
    }
};