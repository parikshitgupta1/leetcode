// day 1 of Leetcode April 2020 Challenge, by Parikshit
// problem Single Number//
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int x = 0;;
        for(int a : nums) {
            x ^= a;
        }
        return x;
    }
};
