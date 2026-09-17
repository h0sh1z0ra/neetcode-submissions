class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        if (n == 0) return 0;

        vector<int> maxLeft(n, 0), maxRight(n, 0);
        int trapped = 0;

        maxLeft[0] = height[0];
        for (int i = 1; i < n; i++)  
            maxLeft[i] = max(maxLeft[i-1], height[i]);

        maxRight[n-1] = height[n-1];
        for (int i = n-2; i >= 0; i--) 
            maxRight[i] = max(maxRight[i+1], height[i]);

        // minimum between the two maxes will be the rain water capable of being trapped
        // min(L,R) - height[i] (round up); always >= 0
        for (int i = 0; i < n; i++) {
            trapped += min(maxLeft[i], maxRight[i]) - height[i];
        }
        return trapped;
    }
};
