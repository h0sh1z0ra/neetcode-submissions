class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        vector<vector<int>> dp(n, vector<int>(2, -1));  // n x 2, all set to -1
        return rec(prices, 0, 0, dp);
    }

private:
    int rec(const vector<int>& prices, int i, int bought, vector<vector<int>>& dp) {
        if (i == prices.size()) return 0; // end of array
        if (dp[i][bought] != -1) return dp[i][bought];

        int result = rec(prices, i+1, bought, dp); // next index
        if (bought == 1) {
            result = max(result, prices[i] + rec(prices, i+1, 0, dp));
        } else {
            result = max(result, -prices[i] + rec(prices, i+1, 1, dp));
        }

        dp[i][bought] = result;
        return result;
    }
};