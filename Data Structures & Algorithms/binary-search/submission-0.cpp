class Solution {
public:
    int search(vector<int>& nums, int target) {
        if (nums.size() == 0) return -1;
        int m = nums.size() / 2;
        if (target == nums[m]) {
            return m;
        } else if (target < nums[m]) {
            vector<int> v(nums.begin(), nums.begin() + m);
            return search(v, target);
        } else {
            vector<int> v(nums.begin() + m + 1, nums.end());
            int a = search(v, target);
            if (a != -1) {
                return a + m + 1;
            }
        }
        return -1;
    }
};
