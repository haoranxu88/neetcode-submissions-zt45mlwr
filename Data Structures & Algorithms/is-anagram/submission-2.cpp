#include <map>
class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        std::map<char, int> maps;
        std::map<char, int> mapt;
        for (int i = 0; i < s.size(); ++i) {
            maps[s.at(i)]++;
            mapt[t.at(i)]++;
        }
        for (const auto& pair : maps) {
            if (maps[pair.first] != mapt[pair.first]) {
                return false;
            }
        }
        return true;
    }
};
