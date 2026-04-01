class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.size() == 0) {
            return 0;
        }
        sort(nums.begin(), nums.end());
        int maxcount = 1; 
        for (int i = 0; i < nums.size(); ++i) {
            int prev = nums[i];
            int count = 1;
            for (int j = i + 1; j < nums.size(); ++j) {
                if (nums[j] - prev == 1) {
                    count++;
                    prev = nums[j];
                }
                if (count > maxcount) {
                    maxcount = count;
                }
            }
        }
        return maxcount;
    }
};
