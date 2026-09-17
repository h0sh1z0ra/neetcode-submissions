class Solution {
public:
    int trap(vector<int>& height) {
        /* 
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
        return trapped; */

        /* Two pointers */

        /*
        Iterate whichever value at each pointer is smaller. The max to the left of the L pointer - height[L] is the water storable.
        The max to the right of the R pointer - height[R] is the water storable.
        */
        int n = height.size();

        int L = 0, R = n-1;
        int maxL = 0, maxR = 0;

        int amountTrapped = 0;

        while (L <= R) {
            if (maxL < maxR) {
                maxL = max(maxL, height[L]);
                amountTrapped += (maxL - height[L] < 0 ? 0 : maxL - height[L]);
                L++;
                
            }
            else {
                maxR = max(maxR, height[R]);
                amountTrapped += (maxR - height[R] < 0 ? 0 : maxR - height[R]);
                R--;
            }
        }
        return amountTrapped;
    }
};
