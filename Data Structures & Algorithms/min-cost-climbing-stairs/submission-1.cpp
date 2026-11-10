// can take 2 steps from the current step, after paying for the value on the current step

// I think I can add 2 extra 0s at the end since they're both 0 cost; we'll go bottom-up DP for this one

// I want dp to be the minimum cost to get to i so far, so the best decision to proceed with is the minimum of dp[i+1] and d[i+2]

class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int n = cost.size();
        vector<int> dp(n+1);

        for (size_t i = 2; i < n+1; i++) {
            dp[i] = min(cost[i-1] + dp[i-1],
                        cost[i-2] + dp[i-2]);
        }

        return dp[n];
    }
};
