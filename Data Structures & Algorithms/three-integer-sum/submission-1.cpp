class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        if (nums.size() < 3) return {};
        vector<vector<int>> vec;
        for (int i = 0; i < nums.size() - 2; ++i) {
            for (int j = i + 1; j < nums.size() - 1; ++j) {
                for (int k = j + 1; k < nums.size(); ++k) {
                    if (nums[i] + nums[j] + nums[k] == 0) {
                        vector<int> v = {nums[i], nums[j], nums[k]};
                        sort(v.begin(), v.end());
                        if (find(vec.begin(), vec.end(), v) == vec.end()) {
                            vec.push_back(v);
                        }
                    }
                }
            }
        }
        return vec;
    }
};
