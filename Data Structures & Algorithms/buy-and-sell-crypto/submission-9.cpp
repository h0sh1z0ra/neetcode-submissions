class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int lowestPrice = prices[0];
        int bestProfit = 0;

        for (const int& sell : prices) {
            bestProfit = max(bestProfit, sell - lowestPrice);
            lowestPrice = min(lowestPrice, sell);
        }

        return bestProfit;
    }
};
