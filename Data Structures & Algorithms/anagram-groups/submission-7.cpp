#include <vector>
#include <iostream>
#include <algorithm>
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::vector<std::vector<std::string>> vec;
        std::vector<std::string> s = strs;
        for(int i = 0; i < strs.size(); ++i) {
            sort(s[i].begin(), s[i].end());
        }
        for (int i = 0; i < strs.size(); ++i) {
            std::vector<std::string> ana = {strs[i]};
            for (int j = i + 1; j < strs.size(); ++j) {
                if (s[i] == s[j]) {
                    ana.push_back(strs[j]);
                    s.erase(s.begin() + j);
                    strs.erase(strs.begin() + j);
                    j--;
                }
            }
            vec.push_back(ana);
        }
        return vec;
    }
};
