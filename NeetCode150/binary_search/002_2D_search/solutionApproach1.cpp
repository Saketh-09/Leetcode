class Solution {
public:

    int getMatrixVal(int val,vector<vector<int>>& matrix, int n){
        int row = val/n;
        int column = val%n;
        return matrix[row][column];
    }
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();
        int n = matrix[0].size();
        int l = 0;
        int r = m*n-1;
        int mid;
        int matVal;
        while (l<=r) {
            mid = (l+r)/2;
            matVal = getMatrixVal(mid,matrix,n);
            if (matVal < target){
                l = mid+1;
            }
            else if(matVal > target){
                r = mid-1;
            }
            else{
                return true;
            }
        }
        return false;
    }
};