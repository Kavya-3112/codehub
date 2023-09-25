class Solution {
public:
    char findTheDifference(string s, string t) {
        char l=0;
        for(char i:s+t)
        {
            l^=i;
        }
        return l;
        
    }
};
