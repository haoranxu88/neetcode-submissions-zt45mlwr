class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> map;
        for (const auto& n : nums) {
            map[n]++;
        }
        unordered_map<int, vector<int>> map2;
        vector<int> freq;
        for (const auto& pair : map) {
            map2[pair.second].push_back(pair.first);
            freq.push_back(pair.second);
        }
        sort(freq.begin(), freq.end(), std::greater<int>());
        vector<int> returnvec;
        for (int i = 0; i < k; ) {
            for (const auto& i : map2[freq[i]]) {
                returnvec.push_back(i);
            }
            i += map2[freq[i]].size();
        }
        return returnvec;
    }
};
