class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxprofit = 0;
        int i = 0;
        for (int k = 1; k < prices.size(); ++k) {
            if (prices[k] < prices[i]) {
                i = k;
            } else if (prices[k] - prices[i] > maxprofit) {
                maxprofit = prices[k] - prices[i];
            }
        }
        return maxprofit;
    }
};
