class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        for (int i = 0; i < 9; ++i) {
            set<char> set;
            for (int j = 0; j < 9; ++j) {
                if (set.count(board[i][j]) > 0 && board[i][j] != '.') {
                    return false;
                } else {
                    set.insert(board[i][j]);
                }
            }
        }
        for (int i = 0; i < 9; ++i) {
            set<char> set;
            for (int j = 0; j < 9; ++j) {
                if (set.count(board[j][i]) > 0 && board[j][i] != '.') {
                    return false;
                } else {
                    set.insert(board[j][i]);
                }
            }
        }
        for (int i = 1; i <= 3; ++i) {
            for (int j = 1; j <= 3; ++j) {
                set<char> set;
                for (int a = 0 + 3*(i -1); a < 3 * i ; ++a) {
                    for (int b = 0 + 3*(j - 1); b < 3 * j; ++b) {
                        if (set.count(board[a][b]) > 0 && board[a][b] != '.') {
                            return false;
                        } else {
                            set.insert(board[a][b]);
                        }
                    }
                }
            }
        }
        return true;
    }
};
