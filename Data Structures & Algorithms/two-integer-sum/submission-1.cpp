class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int one;
        int two;
        for (int i = 0; i < nums.size() - 1; ++i) {
            for (int j = i + 1; j < nums.size(); ++j) {
                if (nums[i] + nums[j] == target) {
                    one = i;
                    two = j;
                }
            }
        }
        std::vector<int> vec = {one, two};
        return vec;
    }
};
