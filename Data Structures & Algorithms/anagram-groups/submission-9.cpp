class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> map;
        for (const auto& s : strs) {
            string key = s;
            sort(key.begin(), key.end());
            map[key].push_back(s);
        }
        vector<vector<string>> vec;
        for (const auto& pair : map) {
            vec.push_back(pair.second);
        }
        return vec;
    }
};
