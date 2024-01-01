class Solution {
public:
    int search(vector<int>& nums, int target) {
        int r = nums.size()-1;
        int l = 0;
        int m;
        while (r>=l) {
            m = l+(r-l)/2;
            cout <<r<<" "<<l <<endl;
            if (target > nums[m]){
                l = m+1;
            }
            else if (target < nums[m]){
                r = m-1;
            }
            else {
                return m;
            }
        }
        return -1;
    }
};