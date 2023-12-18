class Solution {
    public boolean increasingTriplet(int[] nums) {
        int tempI = 0;
        int i = 0;
        int j = -1;
        for(int m=0;m<nums.length;m++){
            if(j>0 && nums[m]>nums[j]){
                return true;
            }
            else if(j==-1){
                if(nums[m]>nums[i]){
                    j = m;
                }
                else if(nums[m]<nums[i]){
                    i = m;
                    tempI = i;
                }
            }
            else if(j>0 && nums[m]<nums[j]){
                if(nums[m]>nums[tempI]){
                    j = m;
                    i = tempI;
                }
                else if(nums[m]<nums[tempI]){
                    tempI = m;
                }
            }
        }
        return false;
    }
}