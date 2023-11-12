class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        std::string merged(word1.size()+word2.size(),'a');
        char ch;
        int ind1=0;
        int ind2=0;
        int i=0;
        while(i<(word1.size()+word2.size())){
            if ((i%2==0 && word1.size()>ind1)||(word2.size()<=ind2)) {
                merged[i] = word1[ind1];
                i += 1;
                ind1 += 1;
            }
            else {
                merged[i] = word2[ind2];
                i += 1;
                ind2 += 1;
            }
        }
        return merged;
    }
};